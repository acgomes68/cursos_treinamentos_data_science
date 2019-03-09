'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
'''
import sys

def myinput(texto):
    retorno = ''
    if sys.version_info.major == 2:
        retorno = raw_input(texto)
    elif sys.version_info.major == 3:
        retorno = input(texto)
    return retorno

qtde = 1
i = 1
while i <= qtde:
    n = myinput('Digite o número correspondente ao dia da semana: ' . format(i))

    if n.isalpha():
        print('O texto "{}" digitado não é um número' . format(n))
    else:
        n = int(n)
        i += 1

if n == 1:
    print('Domingo')
elif n == 2:
    print('Segunda')
elif n == 3:
    print('Terça')
elif n == 4:
    print('Quarta')
elif n == 5:
    print('Quinta')
elif n == 6:
    print('Sexta')
elif n == 7:
    print('Sábado')
else:
    print('Valor Inválido')