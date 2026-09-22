#solicitando nome
nome=input('digite seu nome: ')
idade=int(input('digite sua idade: '))
#criando a condição caso for >= 18 anos
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')