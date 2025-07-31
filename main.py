import os                             
from openai import OpenAI, BadRequestError, AuthenticationError        
from dotenv import load_dotenv     
from ast import literal_eval
import logging

logging.basicConfig(level=logging.INFO)

# Carrega variáveis de ambiente do arquivo .env, sobrescrevendo valores existentes, se necessário
load_dotenv(override=True)

# Obtém o token da API armazenado como variável de ambiente no arquivo .env
AI_API_TOKEN = os.getenv("AI_API_TOKEN")  
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=AI_API_TOKEN,
)

with open("aiConfig.md", "r", encoding="utf-8") as file:
    SYS_CONFIG = file.read()


memory = []

# Função que envia o histórico da conversa e recebe uma resposta da IA
def ai_request(memory: list):
    global assist_memory
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYS_CONFIG,  
                },
                *memory         # Desempacota a lista de mensagens trocadas (usuário e assistente)
            ],
            temperature=1,             # Grau de criatividade (quanto maior, mais criativo)
            top_p=1,                  # Probabilidade acumulada para amostragem (nucleus sampling)
            model=model               # Modelo escolhido
        ).choices[0].message.content

        logging.info(f"Response: {response}")  # Loga a resposta recebida
        
        response = literal_eval(response)
        
        if type(response) != dict or "response" not in response or "function" not in response:
            raise SyntaxError

        assist_memory = True
       
    except (BadRequestError, SyntaxError):
        logging.warning("Bad request or syntax error in response.")
        
        assist_memory = False
        
        memory.pop()
        response = {"response": "", "function": ["erasePrompt"]}
        
        # Incluir script para apagar ultima mensagem enviada pelo usuário na tela
        
    except AuthenticationError:
        logging.error("Authentication error. Check your API token.")
        
        assist_memory = False
        
        memory.pop()
        response = {"response": "Not available now, try later!", "function": []}
    
    finally:
        return response

# Função que registra o prompt do usuário, obtém a resposta da IA e atualiza a memória da conversa
def ai_conversation(user_prompt):
    logging.info(f"Prompt: {user_prompt}")  # Loga a resposta recebida
    
    memory.append({
        "role": "user",
        "content": user_prompt
    })

    json_response = ai_request(memory)
    ai_response = json_response["response"]
    ai_function = json_response["function"]
    
    if assist_memory:
        memory.append({
            "role": "assistant",
            "content": f"{json_response}"
        })

    return (ai_response, ai_function)

while True:
    
    prompt = input("\nVocê: ")             # Recebe entrada do usuário
    ai_response, ai_function = ai_conversation(prompt)   # Obtém resposta da IA (resposta e função)
    print(f"\nIA: {ai_response}")          # Exibe resposta no terminal
    print(f"\nFUNC: {ai_function}")        # Exibe resposta no terminal

