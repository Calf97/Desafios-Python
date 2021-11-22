'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
resp = 'S'
soma = quan = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quan+=1
    resp=str(input('Quer continuar? [S/N]'))
    if quan == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        elif núm < núm:
            menor = núm
média = soma / quan
print('Você digitou {} números a média é {}'.format(quan, média))
print('MAIOR valor {} MENOR valor {}'.format(maior, menor))