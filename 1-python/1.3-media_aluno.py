#criando a variavel nome e as variaveis notas
nome=input('nota do aluno: ')
nota_1=float(input('nota 1: '))
nota_2=float(input('nota 2: '))
nota_3=float(input('nota 3: '))
#calculando a media do aluno
media= (nota_1 + nota_2 + nota_3) / 3
#apresentando o resultado ao usuario
print('a media do aluno(a)', nome, "e", media)