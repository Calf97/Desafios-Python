'''
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
'''
frase = str(input('Digite uma frase: ')).strip().upper() #Strip remove os espaços da frases.
palavras = frase.split() # Divide as palavras
junto = ''.join(palavras) #Ele junta a frase desconsiderando os espaços.
inverso =junto [::-1]
'''for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')

