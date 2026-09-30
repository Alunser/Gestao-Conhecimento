# provedores/gemini.py
import os
from google import genai
from google.genai import types
from .base import ProvedorIAInterface

class GeminiAdapter(ProvedorIAInterface):
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.client = genai.Client()

    def gerar_documentacao(self, dados_squad: str, prompt_sistema: str) -> str:
        response = self.client.models.generate_content(
            model=self.modelo,
            contents=f"Aqui estão os artefatos gerados pela squad:\n\n{dados_squad}",
            config=types.GenerateContentConfig(
                system_instruction=prompt_sistema,
                temperature=0.2,
            ),
        )
        return response.text