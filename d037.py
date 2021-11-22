'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal 
- 3 para hexadecimal 
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[01] converter para BINÁRIO
[02] converter para OCTAL
[03] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Teste novamente.')
