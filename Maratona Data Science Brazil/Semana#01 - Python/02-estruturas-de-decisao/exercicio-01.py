'''
Faça um Programa que peça dois números e imprima o maior deles.
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
qtde = 2

i = 1
while i <= qtde:
    n = myinput('Digite o {}o. número : ' . format(i))

    if n.isalpha():
        print('O texto "{}" do {}o. número não é válido' . format(n, i))
    else:
        lista.append(n)
        i += 1

maior = max(lista)

print('O maior número é', maior)