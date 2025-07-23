import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True) 

API_TOKEN = os.getenv("API_TOKEN") # Puxa o token da API
endpoint = "https://models.github.ai/inference" # Local da API
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=API_TOKEN,
)

BRAIN = """
Modo de resposta:

você deve responder em formato json, da seguinte forma:

{
    "function": "function1"
    "response": "sua resposta aqui"
}

obs. "function" deve ser uma função que corresponde de acordo com o contexto da sua resposta e pergunta do usuário, de acordo com os contextos por funções.
obs2. quando não houver função adequada preencha com none

Funções e Contextos:

{
    "sobre": "O usuário quer saber mais sobre você",
    "ajuda": "O usuário quer ajuda com algo específico",
    "culinaria": "O usuário está interessado em culinária",
    "tecnologia": "O usuário está interessado em tecnologia",
    "entretenimento": "O usuário está interessado em entretenimento",
    "esporte": "O usuário está interessado em esportes",
    "educacao": "O usuário está interessado em educação",
    "saude": "O usuário está interessado em saúde",
    "viagem": "O usuário está interessado em viagens",
}

""" # Personalidade da IA

memory = []


def ai_response(memory:list):

    response = client.chat.completions.create(
        messages=[
            
            {
                "role": "system",
                "content": BRAIN, # Personalidade da IA
            },
            *memory
        ],
        temperature=1,
        top_p=1,
        model=model
    )

    return response.choices[0].message.content   


def ai_conversation(prompt):
    memory.append(
        {
        "role": "user",
        "content": prompt
        }
    )

    response = ai_response(memory)
    memory.append(
        {
        "role": "assistant", 
        "content": response
        }
    )
    
    return response


while True:
    prompt = input("\nVocê: ")
    response = ai_conversation(prompt)
    print(f"\nIA: {response}")

