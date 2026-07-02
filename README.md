# Análise Exploratória de Dados Abertos de Compras Públicas
![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-ETL-150458)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)

Repositório do TCC sobre Análise Exploratória de Dados Abertos de Compras Públicas baseadas na Nova Lei de Licitações (Lei nº 14.133/2021).

## Estrutura do Projeto

| Arquivo | Responsabilidade |
|---|---|
| `licitacoes.ipynb` | Pipeline ETL — leitura dos CSVs, limpeza, merge, feature engineering e salvamento do parquet |
| `eda.ipynb` | Análise exploratória — carrega o parquet e gera as visualizações |
| `viz.py` | Módulo de estilização — paleta Okabe-Ito, configurações de tema e funções de gráfico |
| `DataBases/` | CSVs brutos do comprasGOV (2024 e 2025) |
| `base_analitica_licitacoes_tratada.parquet` | Base analítica final gerada pelo pipeline ETL |

## Como executar

1. Rode `licitacoes.ipynb` do início ao fim para gerar o parquet
2. Abra `eda.ipynb` para explorar as análises — o ETL não precisa ser reexecutado enquanto os dados não mudarem
