'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
total = 0
v = 0

while True:
    jogador = int(input('Digite um número: '))
    PC = randint(1,10)
    total = jogador + PC
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    print(f'Jogador {jogador} + PC {PC} é igual = {total}')
    if tipo == 'P':
       if total % 2 == 0:
           print('Você venceu!')
           v += 1
       else:
           print('Você perdeu')
           break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes.')
