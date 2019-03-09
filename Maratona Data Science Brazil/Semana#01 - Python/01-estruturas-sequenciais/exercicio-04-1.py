'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
n1 = input('Digite a nota do 1o. Bimestre: ')
n2 = input('Digite a nota do 2o. Bimestre: ')
n3 = input('Digite a nota do 3o. Bimestre: ')
n4 = input('Digite a nota do 4o. Bimestre: ')

media = (float(n1) + float(n2) + float(n3) + float(n4)) / 4

print('A média das 4 notas é', str(media))