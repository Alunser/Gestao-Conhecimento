# provedores/__init__.py
from .gemini import GeminiAdapter

def obter_provedor_ia(nome_provedor: str, modelo: str):
    if nome_provedor.lower() == "gemini":
        return GeminiAdapter(modelo=modelo)
    else:
        raise ValueError(f"Provedor de IA desconhecido: {nome_provedor}")