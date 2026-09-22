renda=float(input('digite a sua renda mensal: '))
situação=input('possui restrição/nome negativado (s/n): ')
emprestimo=(renda>=3000) and situação == 'n'
print('emprestimo aprovado', emprestimo)
