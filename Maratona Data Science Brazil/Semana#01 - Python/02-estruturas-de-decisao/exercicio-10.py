'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
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
    l = myinput('Qual o turno você estuda? (M-matutino ou V-Vespertino ou N- Noturno) ')
    if not l.isalpha():
        print('O texto "{}" não é uma letra'.format(l))
    else:
        break

if l.lower() == 'm':
    print('Bom dia!')
elif l.lower() == 'v':
    print('Boa tarde!')
elif l.lower() == 'n':
    print('Boa noite!')
else:
    print('Valor Inválido')