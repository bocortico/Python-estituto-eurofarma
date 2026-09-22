def nome(nome_usuario, sobrenome):
    return f'{nome_usuario} {sobrenome}'

nome_usuario=input('digite seu primeiro nome: ')

sobrenome=input('digite seu sobrenome: ')

nome9 = nome(nome_usuario, sobrenome)

print(f'bem vindo {nome9}')
