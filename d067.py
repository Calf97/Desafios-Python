'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

while True:
    n = int(input('Qual ver a tabuada de qual valor? '))
    if n < 0:
        break
    for x in range(1, 11, ):
            print(f'Tabuada no {n} x {x} = {n * x}')
print('fim')

