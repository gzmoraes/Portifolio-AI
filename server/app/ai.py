import os                           
from openai import OpenAI, BadRequestError, AuthenticationError, RateLimitError
from dotenv import load_dotenv     
import logging
import json


class AIBot(OpenAI):
    def __init__(self):
        self.MODELS = [".1", ".1-mini", ".1-nano", "o", "o-mini"]
        
        logging.basicConfig(level=logging.INFO) # Configura o nível de log para INFO

        # Carrega variáveis de ambiente do arquivo .env, sobrescrevendo valores existentes, se necessário
        load_dotenv(override=True)

        # Obtém o token da API armazenado como variável de ambiente no arquivo .env
        AI_API_TOKEN = os.getenv("AI_API_TOKEN")

        endpoint = "https://models.github.ai/inference"
        
        self.current_model = self.MODELS[0]
        self.model = "openai/gpt-4" + self.current_model

        super().__init__(
            base_url=endpoint,
            api_key=AI_API_TOKEN,
        )

        with open("aiConfig.md", "r", encoding="utf-8") as file:
            self.SYS_CONFIG = file.read()

        self.memory: list[dict[str, str]] = [] # Lista para armazenar o histórico de conversas (mensagens trocadas)
        self.memory_flag: bool = True # Flag para indicar se a memória deve ser atualizada
    
    def ai_conversation(self, user_prompt: str):
        logging.info("Prompt: %s", user_prompt)  # Loga a resposta recebida
        
        self.memory.append({
            "role": "user",
            "content": user_prompt
        })

        dict_response = self.__ai_request()
        
        if self.memory_flag:
            self.memory.append({
                "role": "assistant",
                "content": f"{dict_response}"
            })

        return dict_response
    
    def __ai_request(self):
        try:
            logging.info("Using model %s.", self.model)
            
            ai_raw_response = self.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": self.SYS_CONFIG,  
                    },
                    *self.memory         # Desempacota a lista de mensagens trocadas (usuário e assistente)
                ],

                # functions with no parameters
                tools=[
                    {
                        "type": "function",
                        "function": {
                            "name": "about",
                            "description": "User wants to learn more about, his background, experience, or general information.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "ai_response": {
                                        "type": "string",
                                        "description": "The text response to the user's message."
                                    }
                                }
                            }
                        }
                    },
                    {
                        "type": "function", 
                        "function": {
                            "name": "contact",
                            "description": "User wants to get in touch, ask for contact details, or reach.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "ai_response": {
                                        "type": "string",
                                        "description": "The text response to the user's message."
                                    }
                                }
                            }
                        }
                    },
                    {
                        "type": "function",
                        "function": {
                            "name": "projects", 
                            "description": "User wants to see, learn about, or explore projects.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "ai_response": {
                                        "type": "string",
                                        "description": "The text response to the user's message."
                                    }
                                }
                            }
                        }
                    },
                    {
                        "type": "function",
                        "function": {
                            "name": "services",
                            "description": "User inquires about offerings, services.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "ai_response": {
                                        "type": "string",
                                        "description": "The text response to the user's message."
                                    }
                                }
                            }
                        }
                    },
                    {
                        "type": "function",
                        "function": {
                            "name": "skills",
                            "description": "User wants to know about technical abilities, programming languages, frameworks, or tools.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "ai_response": {
                                        "type": "string",
                                        "description": "The text response to the user's message."
                                    }
                                }
                            }
                        }
                    },
                    {
                        "type": "function",
                        "function": {
                            "name": "socialMedia",
                            "description": "User asks for social media links, profiles, or ways to connect on social platforms.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "ai_response": {
                                        "type": "string",
                                        "description": "The text response to the user's message."
                                    }
                                }
                            }
                        }
                    },
                    {
                        "type": "function",
                        "function": {
                            "name": "feedback",
                            "description": "User asks for feedback, reviews, or what others say about.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "ai_response": {
                                        "type": "string",
                                        "description": "The text response to the user's message."
                                    }
                                }
                            }
                        }
                    }
                ],
                tool_choice="auto",  # Let AI decide which tools to call
                temperature=1,             # Grau de criatividade (quanto maior, mais criativo)
                top_p=1,                  # Probabilidade acumulada para amostragem (nucleus sampling)
                model=self.model               # Modelo escolhido
            ).choices[0].message
        
            # logging.info("Response: %s", ai_raw_response)  # Loga a resposta recebida
            
            response = {}
            if ai_raw_response.tool_calls:
                response["response"] = [json.loads(func.function.arguments)["ai_response"] for func in ai_raw_response.tool_calls]
                logging.info("Parameter responses: %s", response["response"])  # Loga o conteúdo da resposta
                
                if ai_raw_response.tool_calls > 1:
                    self.__new_prompt = "\n\n".join(response["response"])
                    response["response"] = self.__united_response()
                    
                else:
                    response["response"] = response["response"][0]
                
                logging.info("Content response: %s", response["response"])  # Loga o conteúdo da resposta
                    
                response["functions"] = [func.function.name for func in ai_raw_response.tool_calls]
                logging.info("Functions called: %s", response["functions"])  # Loga as funções chamadas
            else:
                response["response"] = ai_raw_response.content
                logging.info("Content response: %s", response["response"])  # Loga o conteúdo da resposta
                
                response["functions"] = []

            # if type(response) != dict or "response" not in response or "function" not in response:
            #     raise SyntaxError

            self.memory_flag = True
            
            return response
        except RateLimitError:
            try:
                logging.warning("%s model exceeded.", self.model)

                self.current_model = + self.MODELS[self.MODELS.index(self.current_model)+1]
                self.model = "openai/gpt-4" + self.current_model
                
                logging.warning("Changed to model %s.", self.model)
                
                return self.__ai_request()
            
            except IndexError:
                logging.error("All models have been exhausted.")
                
                self.memory_flag = False
                
                self.memory.pop()
                return {"response": "Not available now, try later!", "function": ["__reloadPage"]}
        
        except BadRequestError:
            logging.warning("Bad request or syntax error in response.")
            
            self.memory_flag = False
            
            self.memory.pop()
            return {"response": "", "function": ["__erasePrompt"]}
            
        except AuthenticationError:
            logging.error("Authentication error. Check your API token.")
            
            self.memory_flag = False
            
            self.memory.pop()
            return {"response": "Not available now, try later!", "function": ["__reloadPage"]}

    def __united_response(self):
        # Script em andamento
        return "PLACEHOLDER"


# Testando a classe AIBot
if __name__ == "__main__":
    AI = AIBot()
    while True:
        user_input = input("\nVocê: ")             # Recebe entrada do usuário
        AI.ai_conversation(user_input)   # Obtém resposta da IA (resposta e função)

