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
print(f'nota real (gabarito): {nota_real}')
print(f'Nota prevista pela IA: {previsao[0][0]:.2f}')

#-gerando o gráfico de avaliação.

print('---gerando a grafico de disperção (Revisão vs Real)---')

previsões_todas = mp.predict(X_test)
plt.figure(figsize=(6,6))
plt.scatter(Y_test,previsões_todas,color='purple',alpha=0.7)
plt.title('Notas vs Notas previstas pela IA')
plt.xlabel('Nota real (gabarito)')
plt.ylabel('Nota prevista pela IA')
plt.grid(True)

plt.plot([0.1],[0,1],color='red',linestyle='--')
plt.show()