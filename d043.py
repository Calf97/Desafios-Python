'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso 
- Entre 18.5 e 25: Peso ideal 
- 25 até 30: Sobrepeso 
- 30 até 40: Obesidade 
- Acima de 40: Obesidade mórbida
'''

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal.')
elif 18.5 <= imc < 25:
    print('Parabéns você está no PESO normal.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc > 40:
    print('Você está em OBESIDADE mórbida, cuidado!')

