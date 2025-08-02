import os                             
from openai import OpenAI, BadRequestError, AuthenticationError        
from dotenv import load_dotenv     
from ast import literal_eval
import logging


class AIBot(OpenAI):
    def __init__(self):
        logging.basicConfig(level=logging.INFO) # Configura o nível de log para INFO

        # Carrega variáveis de ambiente do arquivo .env, sobrescrevendo valores existentes, se necessário
        load_dotenv(override=True)

        # Obtém o token da API armazenado como variável de ambiente no arquivo .env
        AI_API_TOKEN = os.getenv("AI_API_TOKEN")
        endpoint = "https://models.github.ai/inference"
        self.model = "openai/gpt-4.1"

        super().__init__(
            base_url=endpoint,
            api_key=AI_API_TOKEN,
        )

        with open("aiConfig.md", "r", encoding="utf-8") as file:
            self.SYS_CONFIG = file.read()

        self.memory = []    
    
    def ai_conversation(self, user_prompt: str):
        logging.info(f"Prompt: {user_prompt}")  # Loga a resposta recebida
        
        self.memory.append({
            "role": "user",
            "content": user_prompt
        })

        self.dict_response = self.__ai_request()
        
        if self.memory_flag:
            self.memory.append({
                "role": "assistant",
                "content": f"{self.dict_response["response"]}"
            })

        return self.dict_response
    
    def __ai_request(self):
        try:
            response = self.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": self.SYS_CONFIG,  
                    },
                    *self.memory         # Desempacota a lista de mensagens trocadas (usuário e assistente)
                ],
                temperature=1,             # Grau de criatividade (quanto maior, mais criativo)
                top_p=1,                  # Probabilidade acumulada para amostragem (nucleus sampling)
                model=self.model               # Modelo escolhido
            ).choices[0].message.content

            logging.info(f"Response: {response}")  # Loga a resposta recebida
            
            response = literal_eval(response)
            
            if type(response) != dict or "response" not in response or "function" not in response:
                raise SyntaxError

            self.memory_flag = True
        
        except (BadRequestError, SyntaxError):
            logging.warning("Bad request or syntax error in response.")
            
            self.memory_flag = False
            
            self.memory.pop()
            response = {"response": "", "function": ["erasePrompt"]}
            
        except AuthenticationError:
            logging.error("Authentication error. Check your API token.")
            
            self.memory_flag = False
            
            self.memory.pop()
            response = {"response": "Not available now, try later!", "function": []}
        
        finally:
            return response
    
    
# # Testando a classe AIBot
# if __name__ == "__main__":
#     AI = AIBot()
#     while True:
#         user_prompt = input("\nVocê: ")             # Recebe entrada do usuário
#         response = AI.ai_conversation(user_prompt)   # Obtém resposta da IA (resposta e função)
#         print(f"\nIA: {response["response"]}")          # Exibe resposta no terminal
#         print(f"\nFUNC: {response["function"]}")        # Exibe resposta no terminal
