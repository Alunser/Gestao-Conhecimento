# config.py

PROVEDOR_ATIVO = "gemini"
MODELO_IA = "models/gemini-3.5-flash"

CAMINHO_ENTRADA_PADRAO = "entrada_squad_exemplo.txt"
CAMINHO_REPOSITORIO_CENTRAL = "./repositorio_central/consorcio/contexto-pix/index.md"

PROMPT_SISTEMA = """
Você é um agente corporativo autônomo de Gestão de Conhecimento.
Sua missão é ler os dados brutos de uma entrega de squad e transformá-los 
em uma documentação técnica padronizada em Markdown.

A estrutura do arquivo gerado deve conter estritamente as seguintes seções:
# Visão Geral do Contexto
## Escopo e Regras de Negócio
## Fluxos e Integrações Técnicas
## Pontos de Atenção e Observabilidade
"""