import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('openai_api_key')

openai.api_key = OPENAI_API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your name is Blah-bot and you were built by researchers at NokiaAI."},
        {"role": "user", "content": "did openai train you ?"},
    ]
)

print(response)
