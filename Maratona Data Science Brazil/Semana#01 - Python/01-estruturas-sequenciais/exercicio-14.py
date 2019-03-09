'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso
(peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa
o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''
limite = 50
excesso = 0
multa_excesso = 4
valor_multa = 0

peso = float(input('João, digita o peso dos peixes: '))

if peso > limite:
    excesso = peso - limite
    valor_multa = multa_excesso * excesso
    print("João, você excedeu em {:.2f}Kg o limite de peso que é de {:.2f}Kg" . format(excesso, limite))
else:
    print("João, você NÃO excedeu o limite de peso de {:.2f}Kg".format(limite))

print('Limite: {:.2f} Kg' . format(limite))
print('Peso: {:.2f} Kg' . format(peso))
print('Excesso: {:.2f} Kg' . format(excesso))
print('Multa: R$ {:.2f}' . format(valor_multa))