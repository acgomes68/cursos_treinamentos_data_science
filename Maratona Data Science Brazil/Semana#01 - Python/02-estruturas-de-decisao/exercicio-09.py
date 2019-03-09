'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
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
    n = myinput('Digite o {}o. número: ' . format(i))

    if n.isalpha():
        print('O texto "{}" do {}o. número não é válido' . format(n, i))
    else:
        lista.append(float(n))
        i += 1

lista.sort(reverse=True)

print('A ordem decrescente da lista ficaria assim:', lista)
