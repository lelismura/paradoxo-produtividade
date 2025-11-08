import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def resumo_estatistico(df: pd.DataFrame):
    """
    Exibe resumo estatístico e correlação das variáveis numéricas.
    """
    print("\nResumo estatístico:\n")
    print(df.describe())
    print("\nCorrelação entre variáveis:\n")
    print(df.corr(numeric_only=True))

def grafico_correlacao(df: pd.DataFrame):
    """
    Gera um mapa de calor (heatmap) de correlação.
    """
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="viridis")
    plt.title("Correlação entre métricas de produtividade")
    plt.tight_layout()
    plt.show()
