'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
lista_notas = []
qtde_notas = 4

i = 1
while i <= qtde_notas:
    n = float(input('Digite a nota do {}o. Bimestre: ' . format(i)))
    lista_notas.append(n)
    i += 1

media = sum(lista_notas) / qtde_notas

print('A média das {} notas é {}' . format(qtde_notas, media))