import pandas as pd
from sklearn.preprocessing import StandardScaler as st

#-carregar a base tratada na etapa anterior.
ct = pd.read_csv('conversao_de_tipos.csv')

print('---amostra antes da normalização---')
print(ct.head())

#-escolheremos quais colunas queremos normalizar.
colunas_normalizar = ['idade', 'nota_1', 'nota_2']

#-inicializar o padronizador.
scaler = st()

#-aplicar a normalização nas colunas escolhidas.
ct[colunas_normalizar] = scaler.fit_transform(ct[colunas_normalizar])

print('\n---amostra após a normalização (escalonada)---')
print(ct.head())

#- salvar o arquivo pronto para o treinamento no tensorflow.
ct.to_csv('escala_tensorflow.csv', index=False)
print("\n o dataset esta pronto para alimentar a rede neural.")