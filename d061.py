'''Reforça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 0
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razão
    cont +=1
print('FIM')

