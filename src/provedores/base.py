# provedores/base.py
from abc import ABC, abstractmethod

class ProvedorIAInterface(ABC):
    @abstractmethod
    def gerar_documentacao(self, dados_squad: str, prompt_sistema: str) -> str:
        pass