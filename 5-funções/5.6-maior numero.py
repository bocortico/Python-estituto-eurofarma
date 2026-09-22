#criando função irada...

def maior_numero(X, Y):
    if X > Y:
        return X
    else:
        return Y

#solicitando numeros ultra bigger irados!!!

numero_1 = float(input('digite um numero: '))
numero_2 = float(input('digite outro numero: '))

#chamando a função que representa o maior numero iradicimo!!!

resultado = maior_numero(numero_1, numero_2)

#apresentando o resultado... tambem muito irado!

print(f'o maior numero é {resultado}')
