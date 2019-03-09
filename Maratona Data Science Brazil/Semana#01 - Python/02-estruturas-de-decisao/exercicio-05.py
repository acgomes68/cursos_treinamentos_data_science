'''
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
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
    n = myinput('Digite a {}a. nota: ' . format(i))

    if n.isalpha():
        print('O texto "{}" da {}a. nota não é um número' . format(n, i))
    else:
        n = float(n)
        lista.append(n)
        i += 1

media = sum(lista) / qtde
print('A média das {} notas é {}' . format(qtde, media))

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

