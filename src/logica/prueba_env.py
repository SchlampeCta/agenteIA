import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API Key encontrada correctamente.")
else:
    print("No se encontró la API Key.")