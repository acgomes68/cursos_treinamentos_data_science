'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
import sys

def myinput(texto):
    retorno = ''
    if sys.version_info.major == 2:
        retorno = raw_input(texto)
    elif sys.version_info.major == 3:
        retorno = input(texto)
    return retorno

while True:
    n = myinput('Digite um número: ')
    if n.isalpha():
        print('O texto "{}" não é um número'.format(n))
    else:
        break

nf = float(n)
if nf > 0:
    print('O número {} é positivo' . format(n))
elif nf < 0:
    print('O número {} é negativo'.format(n))
else:
    print('Ahhh, esse é o zero!')
