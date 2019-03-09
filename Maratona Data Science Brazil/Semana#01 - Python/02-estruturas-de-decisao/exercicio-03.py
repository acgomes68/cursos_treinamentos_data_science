'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
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
    l = myinput('Digite uma letra: ')
    if not l.isalpha():
        print('O texto "{}" não é uma letra'.format(l))
    else:
        break

if l.lower() == 'f':
    print('F - Feminino')
elif l.lower() == 'm':
    print('M - Masculino')
else:
    print('Sexo Inválido')