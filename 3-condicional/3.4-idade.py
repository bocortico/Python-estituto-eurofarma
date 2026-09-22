idade=int(input('digite sua idade: '))
nome=input('qual o seu nome: ')
if idade ==0:
    situação='recem nascido'
elif idade <3:
    situação='bebe'
elif idade <10:
    situação="criança"
elif idade <14:
    situação='pré-adolecente/adolecente'
elif idade <30:
    situação='jovem'
elif idade <67:
    situção='adulto'
else:
    situação='idoso'

print(f'{nome} é considerado {situação}.')
