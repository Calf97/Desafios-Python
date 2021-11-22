'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. 
No final, mostre:
A - Qual é total gasto na compra. 
B - Quantos produtos custam mais de R$1000
C - Qual é o nome do produto mais barato.'''

total = quant = caro = barato = 0
while True:
    print('LOJA SUPER BARATÃO')
    print('-' * 30)
    p = str(input('Nome do Pruduto: '))
    v = float(input('Preço: R$ '))
    quant +=1
    total += v

    if quant == 1:
        caro = barato = v
    else:
        if v > caro:
            caro = v
        elif v < barato:
            barato = v

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
        print('-' *30)
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'O produto mais caro custou R${caro:.2f}')
print(f'O produto mais barato custou R${barato:.2f}')