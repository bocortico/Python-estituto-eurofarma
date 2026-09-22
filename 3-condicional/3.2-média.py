#nome e notas do aluno.
nome=input('digite seu nome: ')

nota_1=float(input('digite a primeira nota: '))

nota_2=float(input('digite a segunda nota: '))

nota_3=float(input('digite a terceira nota: '))

#realizando calculo da media.
media=(nota_1 + nota_2 + nota_3)/ 3

if media < 4:
    situação='reprovado'
elif media <= 6:
    situação='recuperação'
else:
    situação='aprovado'

print(f'a media do aluno(a) {nome} é {media:.1f} ele foi {situação}')
