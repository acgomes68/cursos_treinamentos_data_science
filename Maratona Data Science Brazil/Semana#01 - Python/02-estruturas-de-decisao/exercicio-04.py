'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
import sys

def myinput(texto):
    retorno = ''
    if sys.version_info.major == 2:
        retorno = raw_input(texto)
    elif sys.version_info.major == 3:
        retorno = input(texto)
    return retorno

vogais = ['a', 'e', 'i', 'o', 'u']

while True:
    l = myinput('Digite uma letra: ')
    if not l.isalpha():
        print('O caracter "{}" não é uma letra'.format(l))
    else:
        break

if l.lower() in vogais:
    print('Vogal')
elif l.isalpha():
    print('Consoante')
else:
    print('Não é uma letra')