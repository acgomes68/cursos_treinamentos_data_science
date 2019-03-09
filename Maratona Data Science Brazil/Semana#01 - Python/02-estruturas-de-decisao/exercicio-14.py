'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela:
- as notas;
- a média
- o conceito correspondente e;
- a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
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
    n = myinput('Digite a {}a. nota: (0.00 a 10.00): ' . format(i))

    if n.isalpha():
        print('O texto "{}" da {}a. nota não é um número' . format(n, i))
    elif float(n) < 0.00 or float(n) > 10.00:
        print('A nota deve ser um número entre 0 e 10')
    else:
        n = float(n)
        lista.append(n)
        i += 1

media = sum(lista) / qtde

if media <= 4.00:
    conceito = 'E'
elif media > 4.00 and media <= 6.00:
    conceito = 'D'
elif media > 6.00 and media <= 7.50:
    conceito = 'C'
elif media > 7.50 and media <= 9.00:
    conceito = 'B'
else:
    conceito = 'A'

if conceito in ['A', 'B', 'C']:
    mensagem = 'APROVADO'
else:
    mensagem = 'REPROVADO'

for i in range(0, qtde):
    print('{}a. nota: {:.2f}' . format(i + 1, lista[i]))

print('A média das notas é {:.2f}' . format(media))
print('O conceito correspondente é {}' . format(conceito))
print('Situação:', mensagem)
