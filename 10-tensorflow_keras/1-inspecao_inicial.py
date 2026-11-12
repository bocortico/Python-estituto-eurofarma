#-importando a biblioteca pandas com o apelido 'pd'.
import pandas as pd

#-carregando o arquivo .csv sujo
db = pd.read_csv ('dados_brutos.csv')

#2-inspecionar as primeiras linhas.
print('---amostra inicial(head)---')
print(db.head())

#3-inspecionar tipos de dados e quantidades de valores nulos.
print('---informações estruturais(info)---')
print(db.info())

#4-estatisticas descritivas para ver medias e posiveis anomalias.
print('---estatisticas basicas(describe)---')
print(db.describe())

