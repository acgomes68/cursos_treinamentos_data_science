'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
import math

raio = input('Digite o valor do raio da circunferência: ')
area = math.pi * (float(raio)**2)

print('A área da circunferência é de {:.2f}' . format(area))

