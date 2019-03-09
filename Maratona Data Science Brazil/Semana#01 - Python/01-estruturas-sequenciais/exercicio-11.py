'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.
'''
n1 = int(input('Digite a 1o.número (valor inteiro): '))
n2 = int(input('Digite a 2o.número (valor inteiro): '))
n3 = float(input('Digite a 3o.número (valor real): '))

# o produto do dobro do primeiro com metade do segundo
c1 = (n1 * 2) * (n2 / 2)

# a soma do triplo do primeiro com o terceiro.
c2 = (n1 * 3) + n3

# o terceiro elevado ao cubo.
c3 = n3**3

print('O produto do dobro do primeiro número com metade do segundo número é ', str(c1))
print('A soma do triplo do primeiro número com o terceiro número é ', str(c2))
print('O terceiro número elevado ao cubo é {:.2f}' . format(c3))
