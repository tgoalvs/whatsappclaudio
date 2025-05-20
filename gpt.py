import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analisar_como_ceo(texto):
    prompt = f"""
Você é um CEO experiente. Analise a seguinte solicitação:   
"{texto}"

Retorne:
1. Uma lista com os principais tópicos.
2. Um plano de execução baseado nos tópicos.

Formato:
Tópicos:
- item 1
- item 2

Plano de Execução:
1. passo 1
2. passo 2
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    conteudo = response['choices'][0]['message']['content']
    partes = conteudo.split("Plano de Execução:")

    return {
        "topicos": partes[0].replace("Tópicos:", "").strip(),
        "plano": partes[1].strip()
    }