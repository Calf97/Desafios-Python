'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: Junior 
- Até 20 anos: Sênior 
- Acima: MATER
'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: Mirim')

elif idade <= 14:
    print('Classificação: Infantil')

elif idade <= 19:
    print('Classificação: Junior')

elif idade <= 25:
    print('Classificação: Sênior')

else:
    print('Classificação: Master')