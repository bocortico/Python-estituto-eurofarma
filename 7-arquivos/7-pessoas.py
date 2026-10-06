nome= input(' digite seu nome: ')
email=input(' digite seu email: ')

arquivo=open('7-pessoas.txt', 'a')
arquivo.write(f'{nome} | {email} \n')
arquivo.close()
