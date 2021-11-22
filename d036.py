'''
Programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
'''

casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
mínimo = salário * 30 / 100
prestação = casa / (anos * 12)
print('Para pagar uma casa de R${:.2F} reais em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestação))

if prestação <= mínimo:
    print(('O empréstimo pode ser CONCEDIDO!'))
else:
    print('Empréstimo NEGADO!')

