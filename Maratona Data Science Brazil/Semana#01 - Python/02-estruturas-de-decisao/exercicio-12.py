'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor
da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00
'''
import sys

def myinput(texto):
    retorno = ''
    if sys.version_info.major == 2:
        retorno = raw_input(texto)
    elif sys.version_info.major == 3:
        retorno = input(texto)
    return retorno

qtde = 1
i = 1
while i <= qtde:
    vh = myinput('Digite o valor hora em R$: ')

    if vh.isalpha():
        print('O texto "{}" do valor hora não é um número válido' . format(vh))
    elif float(vh) <= 0:
        print('O valor hora deve ser um valor positivo')
    else:
        vh = float(vh)
        i += 1

qtde = 1
i = 1
while i <= qtde:
    qh = myinput('Digite a quantidade de horas trabalhadas: ')

    if qh.isalpha():
        print('O texto "{}" da quantidade de horas trabalhadas não é um valor válido' . format(qh))
    elif float(qh) <= 0:
        print('A quantidade de horas trabalhadas deve ser um valor positivo')
    else:
        qh = int(qh)
        i += 1

salario_bruto = float(vh * qh)
if salario_bruto <= 900.00:
    ir_aliquota = 0.00
elif salario_bruto > 900.00 and salario_bruto <= 1500.00:
    ir_aliquota = 0.05
elif salario_bruto > 1500.00 and salario_bruto <= 2500.00:
    ir_aliquota = 0.10
if salario_bruto > 2500.00:
    ir_aliquota = 0.20

ir_valor = ir_aliquota * salario_bruto

inss_aliquota = 0.10
inss_valor = inss_aliquota * salario_bruto

sindicato_aliquota = 0.03
sindicato_valor = sindicato_aliquota * salario_bruto

fgts_aliquota = 0.11
fgts_valor = fgts_aliquota * salario_bruto

total_descontos = ir_valor + inss_valor + sindicato_valor
salario_liquido = salario_bruto - total_descontos

print('Salário Bruto: (R$ {:.2f} * {})\t\t: R$ {:>8.2f}' . format(vh, qh, salario_bruto))
print('(-) IR ({:>2.0f}%)\t\t\t\t\t\t: R$ {:>8.2f}' . format(ir_aliquota * 100, ir_valor))
print('(-) INSS ({:>2.0f}%)\t\t\t\t\t\t: R$ {:>8.2f}' . format(inss_aliquota * 100, inss_valor))
print('(-) Sindicato({:>2.0f}%)\t\t\t\t\t: R$ {:>8.2f}' . format(sindicato_aliquota * 100, sindicato_valor))
print('FGTS ({:>2.0f}%)\t\t\t\t\t\t\t: R$ {:>8.2f}' . format(fgts_aliquota * 100, fgts_valor))
print('Total de descontos\t\t\t\t\t: R$ {:>8.2f}' . format(total_descontos))
print('Salário Liquido\t\t\t\t\t\t: R$ {:>8.2f}' . format(salario_liquido))
