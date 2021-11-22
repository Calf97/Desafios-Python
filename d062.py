'''Melhore o DESAFIO 061, pergunte para o usuário se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razão
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
