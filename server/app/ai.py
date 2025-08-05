from copy import deepcopy
import os                           
from openai import OpenAI, BadRequestError, AuthenticationError, RateLimitError
from dotenv import load_dotenv     
import logging
import json


class AIBot:
    def __init__(self):
        self.MODELS = [".1", ".1-mini", ".1-nano", "o", "o-mini"]
        
        self.tools = [] # Lista para armazenar as ferramentas (funções) que a IA pode chamar
        self.memory = [] # Lista para armazenar o histórico de conversas (mensagens trocadas)
        self.memory_flag = True # Flag para indicar se a memória deve ser atualizada
        self.ai_raw_response = None # Variável para armazenar a resposta bruta da IA
        
        logging.basicConfig(level=logging.INFO) # Configura o nível de log para INFO

        # Carrega variáveis de ambiente do arquivo .env, sobrescrevendo valores existentes, se necessário
        load_dotenv(override=True)

        # Obtém o token da API armazenado como variável de ambiente no arquivo .env
        AI_API_TOKEN = os.getenv("AI_API_TOKEN")

        endpoint = "https://models.github.ai/inference"
        
        self.current_model = self.MODELS[0]
        self.model = "openai/gpt-4" + self.current_model

        self.AIClient = OpenAI(
            base_url=endpoint,
            api_key=AI_API_TOKEN,
        )

        with open("aiConfig.md", "r", encoding="utf-8") as file:
            self.SYS_CONFIG = file.read()
            
        self._fetch_functions()
    
    def ai_chat(self, user_prompt: str):
        logging.info("Prompt: %s", user_prompt)  # Loga a resposta recebida
        
        self.memory.append({
            "role": "user",
            "content": user_prompt
        })

        dict_response = self._ai_request()
        
        if self.memory_flag:
            self.memory.append({
                "role": "assistant",
                "content": dict_response
            })

        return dict_response
    
    def _fetch_functions(self):
                
        with open("functions.json", "r", encoding="utf-8") as f:
            functions = json.load(f)

        func_model = {
            "type": "function",
            "function": {
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ai_response": {
                            "type": "string",
                            "description": "Text response to the user's message.",
                        }
                    },
                },
            },
        }

        for func_name, func_description in functions.items():

            func_model["function"]["name"] = func_name
            func_model["function"]["description"] = func_description

            self.tools.append(deepcopy(func_model))

        logging.info("Functions: %s", json.dumps(self.tools, indent=2, ensure_ascii=False))  # Loga as funções formatadas como JSON
  
    def _ai_request(self):
        try:
            logging.info("Using model %s", self.model)

            self.ai_raw_response = self.AIClient.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": self.SYS_CONFIG,  
                    },
                    *self.memory        # Desempacota a lista de mensagens trocadas (usuário e assistente)
                ],
                tools=self.tools,
                tool_choice="auto",     # Let AI decide which tools to call
                temperature=1,          # Grau de criatividade (quanto maior, mais criativo)
                top_p=1,                # Probabilidade acumulada para amostragem (nucleus sampling)
                model=self.model        # Modelo escolhido
            ).choices[0].message
             
            return self._process_request()
        
        except RateLimitError:
            return self._handle_rate_limit_error()
        except BadRequestError:
            return self._handle_bad_request_error()
        except AuthenticationError:
            return self._handle_authentication_error()

    def _process_request(self):
            
            response = {}
            if self.ai_raw_response.tool_calls:
                response["response"] = [json.loads(func.function.arguments)["ai_response"] for func in self.ai_raw_response.tool_calls]
                logging.info("Parameter responses: %s", response["response"])  # Loga o conteúdo da resposta
                
                if len(self.ai_raw_response.tool_calls) > 1:
                    self.__new_prompt = "\n\n".join(response["response"])
                    response["response"] = self._unite_responses()
                    
                else:
                    response["response"] = response["response"][0]
                
                logging.info("Content response: %s", response["response"])  # Loga o conteúdo da resposta
                    
                response["functions"] = [func.function.name for func in self.ai_raw_response.tool_calls]
                logging.info("Functions called: %s", response["functions"])  # Loga as funções chamadas
            else:
                response["response"] = self.ai_raw_response.content
                logging.info("Content response: %s", response["response"])  # Loga o conteúdo da resposta
                
                response["functions"] = []

            self.memory_flag = True
            
            return response

    def _unite_responses(self):
        # Script em andamento
        return "PLACEHOLDER"

    def _handle_rate_limit_error(self):
        try:
            logging.warning("%s model exceeded.", self.model)

            self.current_model = self.MODELS[self.MODELS.index(self.current_model)+1]
            self.model = "openai/gpt-4" + self.current_model
            
            logging.warning("Changed to model %s.", self.model)
            
            return self._ai_request()
        
        except IndexError:
            logging.error("All models have been exhausted.")
            
            self.memory_flag = False
            
            self.memory.pop()
            return {"response": "Not available now, try later!", "function": ["_reloadPage"]}

    def _handle_bad_request_error(self):
        logging.warning("Bad request or syntax error in response.")
        
        self.memory_flag = False
        
        self.memory.pop()
        return {"response": "", "function": ["_erasePrompt"]}

    def _handle_authentication_error(self):
        logging.error("Authentication error. Check your API token.")
        
        self.memory_flag = False
        
        self.memory.pop()
        return {"response": "Not available now, try later!", "function": ["_reloadPage"]}        


# Testando a classe AIBot
if __name__ == "__main__":
    AI = AIBot()
    while True:
        user_input = input("\nVocê: ")             # Recebe entrada do usuário
        AI.ai_chat(user_input)   # Obtém resposta da IA (resposta e função)
