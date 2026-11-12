import pandas as pd #-importando a biblioteca pandas com o apelido 'pd'.

#-carregar o arquivo limpo de duplicadas.
ld = pd.read_csv('limpezas_duplicadas.csv')

#-tratamento de inconsistencia de texto.
print('---antes da limpeza de texto---')
print(ld['status_matriculado'].unique())

#-padronizar: .str.strip() - remove espaços extras nas pontas e .str.lower() - padroniza tudo para minusculo
ld['status_matriculado'] = ld['status_matriculado'].str.strip().str.lower()

print('---depois da limpeza de texto---')
print(ld['status_matriculado'].unique())