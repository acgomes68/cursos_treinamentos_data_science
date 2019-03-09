'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''
temperatura_celsius = input('Digite a temperatura em graus Celsius: ')
temperatura_farenheit  = (float(temperatura_celsius) * 9 / 5) + 32

print('A temperatura em graus Farenheit é {:.2f}' . format(temperatura_farenheit))
