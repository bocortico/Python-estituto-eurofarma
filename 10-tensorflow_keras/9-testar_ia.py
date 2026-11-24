import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras

#-carregar os dados de teste.
print('---carregando dados de teste---')
X_test = pd.read_csv('X_teste.csv')
Y_test = pd.read_csv('Y_teste.csv')

#-carregar o cerebro da IA ja salva.
print('carregar o modelo já salvo (.keras)')
mp = keras.models.load_model('analizador_notas_v3_19112026.keras')
print('---modelo carregado com sucesso na memória do computador')

#-avaliar o modelo (a prova final).
print('\n ---avaliando a IA com os dados que ela nunca viu---')
resultado_test = mp.evaluate(X_test,Y_test)
print(f'perda (Loss) oficial no teste: {resultado_test}')

#-fazer uma prvisão de um aluno novo.
print('\n---fasendo uma previsão real---')
#-pegando apenas o primeiro aluno de base de teste para simular um caso real.
aluno_exemplo = X_test.head(1)
nota_real = Y_test.head(1)

#-a IA faz a previsão.
previsao = mp.predict(aluno_exemplo)



print(f'Dados dos analizados: \n{aluno_exemplo}')
print(f'nota real (gabarito): {nota_real[0]}')
print(f'Nota prevista pela IA: {previsao[0][0]:.2f}')
