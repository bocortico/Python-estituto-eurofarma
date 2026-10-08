dados_tabela= [['bairro', 'cidade', 'estado', 'CEP'],['jardim belval', 'barueri', 'SP', '064200'],['parque santana', 'santana de parnaiba', 'sp', '1089004'],['suburbano', 'itapevi', 'SP', '0659373']]

with open ('7.02 - cidade csv', 'w', encoding ='utf-8', newline="") as arquivo_csv:
    escrevendo= CSV.writter(arquivo_csv)
    escrevendo.writerows(dados_tabela)
