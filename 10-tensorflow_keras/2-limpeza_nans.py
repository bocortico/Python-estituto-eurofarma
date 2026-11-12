import pandas as pd #-importando novamente a biblioteca pandas com o apelido 'pd'.

#-caregando o arquivo bruto.
df = pd.read_csv('dados_brutos.csv')

#-verificar quantos valores nulos temos antes do tratamento.
print('---valores nulos antes---')
print(df.isnull().sum())

#-preencher valores ausentes nas notas com a mediana da respectiva coluna.
mediana_nota1 = df['nota_1'].median() 
df['nota_1'] =df['nota_1'].fillna(mediana_nota1)

mediana_nota2 = df['nota_2'].median() 
df['nota_2'] =df['nota_2'].fillna(mediana_nota2)

mediana_idade = df['idade'].median() 
df['idade'] =df['idade'].fillna(mediana_idade)

#-verificar se ainda restam nulos apos o tratamento.
print('---valores nulos depois---')
print(df.isnull().sum())

#-grava arquivo novo sem capos NaNs.
df .to_csv('dados_sem_NaNs.csv', index=False)