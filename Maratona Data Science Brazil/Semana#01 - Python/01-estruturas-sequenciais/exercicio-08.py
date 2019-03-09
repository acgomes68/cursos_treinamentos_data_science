'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''
valor_hora = input('Qual o seu valor hora? ')
horas_mes = input('Quantas horas trabalhadas no mês? ')

salario = float(valor_hora) * int(horas_mes)

print('O total do salário para o período é de {:.2f}' . format(salario))