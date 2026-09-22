#solicitando nome

nome=input('digite seu nome: ')
idade=int(input('digite sua idade: '))

#criando a condição caso for >= 18 anosif idade >= 18:

if idade >= 18:
    posui_carteira=input('possui carteira de motorista s/n: ')
    if posui_carteira == 's':
        print('pode dirigir')
    else:
        print('não pode dirigir')

else:
    print('menor de idade')
