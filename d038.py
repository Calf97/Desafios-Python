'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior 
- O segundo valor é maior 
- Não existe valor maior, os dois são iguais
'''
# Entrada de dados
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

#Verificação
if n1 > n2:
    print('O primeiro número é MAIOR')
elif n2 > n1:
    print('O segundo número é MAIOR')
else:
    print('Os dois valores são iguais')

