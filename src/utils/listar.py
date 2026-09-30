import os
from dotenv import load_dotenv
from google import genai

# Carrega a chave do .env
load_dotenv()

# Conecta na API
client = genai.Client()

print("🔍 Buscando modelos disponíveis para a sua chave...\n")

# Usa o método list() que é o correto no novo SDK
for model in client.models.list():
    if "flash" in model.name:
        print(f"✅ Modelo liberado: {model.name}")