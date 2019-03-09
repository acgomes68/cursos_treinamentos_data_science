'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:
- 11% para o Imposto de Renda;
- 8% para o INSS;
- 5% para o sindicato

Faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
- calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
ir_aliquota = 0.11
ir_valor = 0
inss_aliquota = 0.08
inss_valor = 0
sindicato_aliquota = 0.05
sindicato_valor = 0
descontos = 0
salario_bruto = 0
salario_liquido = 0

valor_hora = input('Qual o seu valor hora? ')
horas_mes = input('Quantas horas trabalhadas no mês? ')

salario_bruto = float(valor_hora) * int(horas_mes)
ir_valor = ir_aliquota * salario_bruto
inss_valor = inss_aliquota * salario_bruto
sindicato_valor = sindicato_aliquota * salario_bruto
descontos = ir_valor + inss_valor + sindicato_valor
salario_liquido = salario_bruto - descontos

print('#### VENCIMENTOS ####')
print('\tSalário bruto: R$ {:.2f}' . format(salario_bruto))
print('Total de Vencimento: R$ {:.2f}' . format(salario_bruto))
print()
print('#### DESCONTOS ####')
print('\tValor IR ({:.2f}%): R$ {:.2f}' . format(ir_aliquota * 100, ir_valor))
print('\tValor INSS ({:.2f}%): R$ {:.2f}' . format(inss_aliquota * 100, inss_valor))
print('\tValor Sindicato({:.2f}%): R$ {:.2f}' . format(sindicato_aliquota * 100, sindicato_valor))
print('Total de Descontos: R$ {:.2f}' . format(descontos))
print()
print('Valor Líquido (Vencimentos - Descontos): R$ {:.2f}' . format(salario_liquido))
