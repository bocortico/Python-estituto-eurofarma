import pandas as pd
import tensorflow as tf
from tensorflow import keras

#-carregamento de dados de treinamento da intêligencia de tensorflow.

print('---carregandos os dados')
X_train = pd.read_csv('X_treino.csv')
X_test = pd.read_csv('X_teste.csv')
Y_train = pd.read_csv('Y_treino.csv')
Y_test = pd.read_csv('Y_teste.csv')

#-desenhando a estrutura do nosso modelo de inteligência tensorflow.

#-modelo sequencial e os neurônios (O desenho da planta baixa).
modelo = keras.Sequential(
    [
    #-primeira camada:10 neurônios que recebem a coluna de entrada (X_train)
    keras.layers.Dense(10, activation='relu', input_shape = [X_train.shape[1]]),
    keras.layers.Dense(1)
    ]
)

#-as regras de erro  e otimzação (0 compile)
modelo.compile(
    optimizer = 'adam',
    loss = 'mse'

)

#-treinamento da inteligência artifial (a aula pratica).
print('---iniciando o treinamento da inteligência artificial---')

#-o metodo .fit é onde a magica acontece: entragamos as pistas e o gabarito.
histórico = modelo.fit(
    X_train,
    Y_train,
    epochs = 1000,
    verbose = 5
)

print('\n treinamento concluido com sucesso! a IA aprendeu os padrões.')

#-salvando o modelo de treinamento.
print('---salvando cérebro de IA em arquivo---')
modelo.save('analizador_notas_v3_19112026.keras')
print('---modelo salvo com sucesso como "modelo_notas.keras"')