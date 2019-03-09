'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
'''
altura = input('Digite a altura da pessoa: ')

peso_ideal = (72.7 * float(altura)) - 58

print('O peso ideal para essa pessoa é {:.2f}' . format(peso_ideal))