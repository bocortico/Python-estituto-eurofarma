def calculo1(X, Y):
    soma = X + Y
    return soma

def calculo2(X, Y):
    multiplicação = X * Y
    return multiplicação

def calculo3(X, Y):
    subtração = X - Y
    return subtração

def calculo4(X, Y):
    divisão = X / Y
    return divisão

numero_1 = float(input('digite um numero: '))
numero_2 = float(input('digite o segundo numero: '))

resulta_soma=calculo1(numero_1, numero_2)
resultado_mul=calculo2(numero_1, numero_2)
resultado_sub=calculo3(numero_1, numero_2)
resultado_div=calculo4(numero_1, numero_2)

print(f'resultado da soma: {resulta_soma}')
print(f'reslutado da multiplicação: {resultado_mul}')
print(f'reslutado da subtração: {resultado_sub}')
print(f'reslutado da divisão: {resultado_div}')

