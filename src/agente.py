# agente.py
import os
from dotenv import load_dotenv
from config import PROVEDOR_ATIVO, MODELO_IA, CAMINHO_ENTRADA_PADRAO, CAMINHO_REPOSITORIO_CENTRAL, PROMPT_SISTEMA
from provedores import obter_provedor_ia

load_dotenv()

def executar_agente_curadoria():
    print("🚀 [SIMULAÇÃO DE PIPELINE] Merge detectado na branch 'main'!")
    print(f"🤖 Iniciando o Agente utilizando o provedor: [{PROVEDOR_ATIVO.upper()}]...")

    try:
        ia = obter_provedor_ia(PROVEDOR_ATIVO, MODELO_IA)
    except Exception as e:
        print(f"❌ Erro ao instanciar provedor de IA: {e}")
        return

    if not os.path.exists(CAMINHO_ENTRADA_PADRAO):
        with open(CAMINHO_ENTRADA_PADRAO, "w", encoding="utf-8") as f:
            f.write("""
            [Feature: Pix Antecipado de Consórcio]
            - Regra de Negócio: O cliente pode antecipar parcelas do consórcio utilizando Pix.
            - Impacto: Concede desconto de 5% sobre os juros vincendos do saldo devedor.
            """)

    with open(CAMINHO_ENTRADA_PADRAO, "r", encoding="utf-8") as f:
        dados_squad = f.read()

    print("🧠 Processando conhecimento estruturado via adaptador...")

    try:
        markdown_resultado = ia.gerar_documentacao(dados_squad, PROMPT_SISTEMA)
        
        os.makedirs(os.path.dirname(CAMINHO_REPOSITORIO_CENTRAL), exist_ok=True)
        with open(CAMINHO_REPOSITORIO_CENTRAL, "w", encoding="utf-8") as f:
            f.write(markdown_resultado)

        print(f"🎉 SUCESSO! Documentação salva em: {CAMINHO_REPOSITORIO_CENTRAL}")
        
    except Exception as e:
        print(f"\n❌ ERRO NA CHAMADA DA IA: {e}")

if __name__ == "__main__":
    executar_agente_curadoria()