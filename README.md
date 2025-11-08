# 🧠 Paradoxo da Produtividade  
**Análise comparativa entre ferramentas No-Code/Low-Code e bibliotecas Python/R**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17535978.svg)](https://doi.org/10.5281/zenodo.17535978)
![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📘 Descrição

Este repositório contém os códigos, dados e documentos associados ao estudo  
**“O Paradoxo da Produtividade: Avaliando o Trade-off entre Ferramentas Visuais e Bibliotecas de Código (Python/R)”**.

O projeto investiga como ferramentas **No-Code/Low-Code** (ex: Power BI Query Editor, Tableau Prep) se comparam a abordagens **baseadas em código** (Python, R) em termos de produtividade, reprodutibilidade e manutenção.

O repositório foi criado para suportar tanto o artigo teórico quanto o estudo empírico futuro — que analisará **dados de produtividade e desempenho real de pipelines visuais e programáticos**.

---

## ⚙️ Estrutura do Projeto
paradoxo-produtividade/
├── dados/
│ ├── cru/ # Dados originais (não processados)
│ └── processado/ # Dados tratados e prontos para análise
├── src/ # Código-fonte (scripts Python)
│ ├── carregar_dados.py
│ └── analise_produtividade.py
├── cadernos/ # Notebooks Jupyter (experimentos)
├── reports/ # Relatórios e figuras geradas
├── requirements.txt # Dependências do ambiente
├── setup.cfg # Metadados e empacotamento
├── LICENSE # Licença MIT
└── zenodo.json # Metadados para Zenodo (DOI, autor, etc.)
---

## 🚀 Como Executar

### Instalar dependências

**Usando pip:**
```bash
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows
pip install -r requirements.txt

mamba env create -f environment.yml
mamba activate paradoxo

Rodar um teste rápido

Baixar dados de amostra (PETR4, BBAS3, VALE3 e USDBRL) e salvar em dados/processado:

python src/fetch_sample.py


Gerar resumo e gráficos:

python -m src.analise_produtividade

📊 Exemplo de saída esperada

Resumo estatístico com médias e desvios-padrão das séries.

Correlação entre variáveis exibida em formato tabular.

Mapa de calor (heatmap) das correlações entre ativos.

(As figuras são salvas automaticamente em /reports/figures/.)

🧩 Objetivo Científico

O estudo busca responder empiricamente:

“Ferramentas visuais realmente aumentam a produtividade em longo prazo ou apenas mascaram a complexidade do processo analítico?”

Os experimentos futuros irão comparar:

Tempo de execução de tarefas visuais vs. codificadas

Reprodutibilidade dos resultados

Complexidade de manutenção dos fluxos

🧾 Citação

Se utilizar este repositório, cite da seguinte forma:

Murakami, Lelis (2025).
Paradoxo da Produtividade: Impactos das Ferramentas No-Code e Low-Code.
DOI: 10.5281/zenodo.17535978

Licença: MIT.

📜 Licença

Este projeto está licenciado sob os termos da Licença MIT
.

🧭 Contato

Autor: Lelis Murakami

Instituição: FATEC / Centro Paula Souza
Repositório: GitHub – lelimura/paradoxo-produtividade


