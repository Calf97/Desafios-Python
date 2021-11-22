'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento. 

Seu programa também deverá mostrar o tempo que falta ou se passoou do prazo. 
'''
	
from datetime import date
atual = date.today().year
nasc = int(input('Em qual ano nasceu? '))
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos no ano de {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Ano de alistamento')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda não chegou sua vez, ainda faltam {} anos'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} ano'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano.'.format(ano))