#solicitando peso e altura
peso=float(input('digite seu peso em (kg) por favor: '))
altura=float(input('digite sua altura (m) por favor: '))

#realizando o calculo do imc
imc=peso / altura**2

#apresentando o resultado ao usuario
print('o imc é ' , imc)