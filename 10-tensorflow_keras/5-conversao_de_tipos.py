import pandas as pd

#-carregar a base de dados tratada na etapa anterior.
li = pd.read_csv('limpezas_inconsistencias_outliers.csv')

print('---antes do encoding(status_matriculado)---')
print(li['status_matriculado'].head())

#-transformando textos em numeros binarios (0 e 1).
li['status_matriculado'] = li['status_matriculado'].map({'sim': 1, 'não': 0})

print('---após o encoding(status_matriculado)---')
print(li['status_matriculado'].head())

#-salvando o resultado final para o tensorflow.
li.to_csv('conversao_de_tipos.csv', index=False)
print("\n variaveis codificadas e arquivo salvo com sucesso: 'conversao_de_tipos.csv' criado no diretório." )
