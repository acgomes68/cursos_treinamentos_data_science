'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''
import sys

def myinput(texto):
    retorno = ''
    if sys.version_info.major == 2:
        retorno = raw_input(texto)
    elif sys.version_info.major == 3:
        retorno = input(texto)
    return retorno

lista = []
qtde = 3

i = 1
while i <= qtde:
    n = myinput('Digite o preço do {}o. produto: ' . format(i))

    if n.isalpha():
        print('O texto "{}" do {}o. produto não é um número válido' . format(n, i))
    else:
        lista.append(n)
        i += 1

menor = min(lista)

print('O produto que você deve comprar é o que custa R$ {:.2f}' . format(float(menor)))