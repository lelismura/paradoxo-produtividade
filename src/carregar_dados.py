import pandas as pd
import os

def carregar_dados(caminho: str) -> pd.DataFrame:
    """
    Carrega arquivos CSV ou Excel a partir do diretório especificado.
    Retorna um DataFrame pandas.

    Parâmetros:
    ----------
    caminho : str
        Caminho completo do arquivo.

    Retorna:
    -------
    pd.DataFrame
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    if caminho.endswith(".csv"):
        return pd.read_csv(caminho)
    elif caminho.endswith((".xls", ".xlsx")):
        return pd.read_excel(caminho)
    else:
        raise ValueError("Formato de arquivo não suportado. Use .csv ou .xlsx")
