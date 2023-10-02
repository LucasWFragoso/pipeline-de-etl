import os
import openai
from dotenv import load_dotenv
from extractIds import users

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em markting bancário.",
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para nosso cliente, contando sobre investimento. Comece com assim: {user['name']}... (máximo de 100 caracteres)",
            },
        ],
    )
    return completion.choices[0].message.content.strip('/"')
