import pandas as pd #-importando a biblioteca pandas com o apelido 'pd'.

#-carregar o arquivo limpo de duplicadas.
ld = pd.read_csv('limpezas_duplicadas.csv')

#-tratamento de inconsistencia de texto.
print('---antes da limpeza de texto---')
print(ld['status_matriculado'].unique())

#-padronizar: .str.strip() - remove espaços extras nas pontas e .str.lower() - padroniza tudo para minusculo
ld['status_matriculado'] = ld['status_matriculado'].str.strip().str.lower()

#-mostras os valores unicos depois da limpesa de texto.
print('---depois da limpeza de texto---')
print(ld['status_matriculado'].unique())

#-tratamento de outliers.
#filtra e mantem apenas alunos com idades validas.
ld = ld[(ld['idade'] > 16) & (ld['idade'] < 50)]

#-corrige de forma cirurgica notas invalidas.
ld.loc[ld['nota_1'] > 10, 'nota_1'] = 10
ld.loc[ld['nota_1'] < 0, 'nota_1'] = 0

ld.loc[ld['nota_2'] > 10, 'nota_2'] = 10
ld.loc[ld['nota_2'] < 0, 'nota_2'] = 0

print('---textos padronizados e outliers tratados com sucesso---')

#-exibindo os resultados após a limpeza.
#-mostra o novo painel estatistico.
print('\n---estatistica atualizada apóa tratar os outliers---')
print(ld.describe())
#-mostrar quantas linhas sobraram na tabela apóas os cortes de idade.
print(f'total de linhas validas após os filtros {len(ld)}')

#-gravando a nova versão no disco.
ld.to_csv('limpezas_inconsistencias_outliers.csv', index=False)
print("\n arquivo salvo com sucesso: 'limpezas_inconsistencias_outliers.csv' criado no diretório.")