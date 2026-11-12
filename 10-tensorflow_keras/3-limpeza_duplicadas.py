import pandas as pd #-importando a biblioteca pandas com o apelido 'pd'.

#-carregar o arquivo sem NaNs.
dn = pd.read_csv('dados_sem_NaNs.csv')

#-verificar o numero de linhas antes de remover duplicadas.
print(f'---total de linhas antes da limpeza de duplicadas {len(dn)}---')

#-filtrar e exibir apenas as linhas duplicadas.
linhas_duplicadas = dn[dn.duplicated(keep=False)]

print('---linhas duplicadas---')
print(linhas_duplicadas)

#-removendo linhas que são copias fieis umas das outras.
dn.drop_duplicates(inplace = True)

#-verificar o numero de linhas apos  a remoção das duplicadas.
print(f'---total de linhas apos a remoção das duplicadas {len(dn)}---')

#-salvar o resultado das linhas apos a remoção.
dn.to_csv('limpezas_duplicadas.csv', index=False)