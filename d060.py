'''Faça um programa que leia um número qualquer e mostre o seu fatorial. 
'''

from math import factorial
import time
tempo_inicial = time.time()# Em segundos
#No meio do tempo_inicial e tempo_final fica meu código.
num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1

for num in range(num, 0, -1):
   f *= num
   print('{}'.format(num), end='')
   print(' X ' if num > 1 else ' = ', end=' ')
print('\n{}'.format(f))

tempo_final = time.time()
print(f"O código demorou {tempo_final - tempo_inicial} milissegundos")




