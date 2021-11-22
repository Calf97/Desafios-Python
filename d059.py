'''
Crie um programa que leia dois valores e mostre em menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resulta entre {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('O primeiro valor é maior')
        elif n2 > n1:
            maior = n2
            print('O segundo valor é maior')
        elif n1 == n2:
            print('Os dois valores são iguais')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('finalizando')
    else:
        print('Opção inválida. Tente novamente.')
        print('-=-' * 10)
print('Fim do programa! Volte sempre!')








