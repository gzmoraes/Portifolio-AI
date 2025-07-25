import os                             
from openai import OpenAI             
from dotenv import load_dotenv        
import json


# Carrega variáveis de ambiente do arquivo .env, sobrescrevendo valores existentes, se necessário
load_dotenv(override=True)

# Obtém o token da API armazenado como variável de ambiente no arquivo .env
API_TOKEN = os.getenv("API_TOKEN")  
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=API_TOKEN,
)

with open("aiBrain.md", "r", encoding="utf-8") as file:
    BRAIN = file.read()


memory = []

# Função que envia o histórico da conversa e recebe uma resposta da IA
def ai_request(memory: list):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": BRAIN,  
            },
            *memory               # Desempacota a lista de mensagens trocadas (usuário e assistente)
        ],
        temperature=1,            # Grau de criatividade (quanto maior, mais criativo)
        top_p=1,                  # Probabilidade acumulada para amostragem (nucleus sampling)
        model=model               # Modelo escolhido
    )

    # Retorna apenas o conteúdo da resposta da IA
    json_response = json.loads(response.choices[0].message.content)

    return json_response

# Função que registra o prompt do usuário, obtém a resposta da IA e atualiza a memória da conversa
def ai_conversation(prompt):
    memory.append({
        "role": "user",
        "content": prompt
    })

    json_response = ai_request(memory)
    ai_response = json_response["response"]
    ai_function = json_response["function"]
    
    #print(f"Função chamada: {ai_function}")  # Exibe a função chamada pela IA, se houver
    
    memory.append({
        "role": "assistant",
        "content": ai_response
    })

    return (ai_response, ai_function)

while True:
    prompt = input("\nVocê: ")           # Recebe entrada do usuário
    ai_response, ai_function = ai_conversation(prompt)   # Obtém resposta da IA (resposta e função)
    print(f"\nIA: {ai_response}")           # Exibe resposta no terminal


