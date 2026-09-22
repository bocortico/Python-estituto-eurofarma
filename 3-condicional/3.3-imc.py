peso=float(input('digite seu peso em (kg) por favor: '))
nome=input('qual o seu nome: ')
altura=float(input('digite sua altura: '))
#realizando o calculo do imc
imc=peso / altura**2

#apresentando o resultado ao usuario
if imc < 18:
    situação='esta abaixo do peso.'
elif imc <=18:
    situação='esta no peso normal.'
elif imc <=29:
    situação='esta com excesso de peso.'
elif imc <=39:
    situação='esta obeso(a)'
else:
    situação='esta muito obeso(a).'

print(f'o paciente {nome} tem o imc de: {imc:.2f} e {situação}.')