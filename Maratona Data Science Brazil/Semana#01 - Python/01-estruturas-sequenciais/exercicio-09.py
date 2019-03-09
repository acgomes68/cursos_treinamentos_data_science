'''
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''
temperatura_farenheit = input('Digite a temperatura em graus Farenheit: ')
temperatura_celsius = (5 * (float(temperatura_farenheit)-32) / 9)

print('A temperatura em graus Celsius é {:.2f}' . format(temperatura_celsius))
