'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
- Para homens: (72.7*h) - 58
- Para mulheres: (62.1*h) - 44.7
'''
altura = input('Digite a altura da pessoa: ')
genero = ''

while genero not in ['M', 'm', 'F', 'f']:
    genero = input('Digite <M> se essa pessoa for um homens ou <F> se essa pessoa for uma mulher: ')

    if (genero not in ['M', 'm', 'F', 'f']):
        print('Digite apenas M ou F')

if genero in ['M', 'm']:
    peso_ideal = (72.7 * float(altura)) - 58
else:
    peso_ideal = (62.1 * float(altura)) - 44.7

print('O peso ideal para essa pessoa é {:.2f}' . format(peso_ideal))
