import pandas as pd
from sklearn.model_selection import train_test_split

#-carregar a base tratada e normalizada na etapa anterior.
df = pd.read_csv('escala_tensorflow.csv')

#-separando as colunas dos arquivos X e Y.
X = df.drop(columns = ['nome', 'id_aluno', 'email', 'nota_2'])
Y = df['nota_2']

print('---imprimindo a primeira linha do X---')
print(X.head(5))

print('---imprimindo a primeira linha do Y---')
print(Y.head(5))

#-dividir os dados 80% para treino e 20% para teste.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print('\n Dados divididos e prontos para alimentar a rede neural do tensorflow.')

#-gravando os 4 arquivos usado para treino e teste da rede neural.
X_train.to_csv('X_treino.csv', index=False)
X_test.to_csv('X_teste.csv', index=False)
Y_train.to_csv('Y_treino.csv', index=False)
Y_test.to_csv('Y_teste.csv', index=False)
