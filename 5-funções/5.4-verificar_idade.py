def verificar_idade(idade):
    if idade>= 18:
        return 'maior de idade'
    else:
        return 'menor de idade'

idade_usuario=int(input(' digite sua idade: '))

resultado=verificar_idade(idade_usuario)

print(resultado)