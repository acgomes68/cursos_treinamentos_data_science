'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o preço seja o menor;
- Acrescente 10% de folga e;
- sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
cobertura_tinta = 6
folga = 0.10
qtde_tinta_necessaria = 0.00
qtde_tinta_folga = 0.00

qtde_lata_tinta = 18
preco_lata_tinta = 80

qtde_galao_tinta = 3.6
preco_galao_tinta = 25

qtde_latas_necessarias = 0
preco_total_latas = 0.00

qtde_galoes_necessarios = 0
preco_total_galoes = 0.00

preco_total_geral = 0.00

tamanho_area = float(input('Qual o tamanho da área a ser pintada em m2? '))

# Calcula a qtde de tinta necessária para cobrir a área descrita
qtde_tinta_necessaria = tamanho_area / cobertura_tinta

# Calcula a folga de quantidade de tinta
qtde_tinta_folga = qtde_tinta_necessaria * folga

# Adiciona a folga de quantidade de tinta à quantidade real necessária
qtde_tinta_necessaria += qtde_tinta_folga

# Calcular a qtde e o preço usando apenas latas de 18l
if qtde_tinta_necessaria <= qtde_lata_tinta:
    qtde_latas_necessarias = 1
else:
    qtde_latas_necessarias = int(qtde_tinta_necessaria / qtde_lata_tinta)
    if (qtde_tinta_necessaria % qtde_lata_tinta > 0):
        qtde_latas_necessarias += 1
preco_total_latas = qtde_latas_necessarias * preco_lata_tinta
preco_total_geral = preco_total_latas

print('#### SOMENTE LATAS DE 18L ####')
print('Quantidade de latas de 18l necessárias:', str(qtde_latas_necessarias))
print('Preço total de latas de 18l : R$ {:.2f}' . format(preco_total_latas))
print('PREÇO TOTAL: R$ {:.2f}' . format(preco_total_geral))
print()

# Calcular a qtde e o preço usando apenas galões de 3.6l
if qtde_tinta_necessaria <= qtde_galao_tinta:
    qtde_galoes_necessarios = 1
else:
    qtde_galoes_necessarios = int(qtde_tinta_necessaria / qtde_galao_tinta)
    if (qtde_tinta_necessaria % qtde_galao_tinta > 0):
        qtde_galoes_necessarios += 1
preco_total_galoes = qtde_galoes_necessarios * preco_galao_tinta
preco_total_geral = preco_total_galoes

print('#### SOMENTE GALÕES DE 3.6L ####')
print('Quantidade de galões de 3.6l necessários:', str(qtde_galoes_necessarios))
print('Preço total de galões de 3.6l: R$ {:.2f}' . format(preco_total_galoes))
print('PREÇO TOTAL: R$ {:.2f}' . format(preco_total_geral))
print()

# Calcular a qtde e o preço usando latas de 18l e galões de 3.6L
for qtd_lata in range(1, qtde_latas_necessarias):
    for qtd_galao in range(1, qtde_galoes_necessarios):
        qtde_tinta = (qtd_lata * qtde_lata_tinta) + (qtd_galao * qtde_galao_tinta)
        if (qtde_tinta >= qtde_tinta_necessaria):
            preco_total_geral = (qtd_lata * preco_lata_tinta) + (qtd_galao * preco_galao_tinta)
            break
    if preco_total_geral > 0.00:
        break;

qtde_latas_necessarias = qtd_lata
preco_total_latas = qtde_latas_necessarias * preco_lata_tinta

qtde_galoes_necessarios = qtd_galao
preco_total_galoes = qtde_galoes_necessarios * preco_galao_tinta

print('#### LATAS DE 18L E GALÕES DE 3.6L####')

print('Quantidade de latas de 18l necessárias:', str(qtde_latas_necessarias))
print('Preço total de latas de 18l: R$ {:.2f}' . format(preco_total_latas))

print('Quantidade de galões de 3.6l necessários:', str(qtde_galoes_necessarios))
print('Preço total de galões de 3.6l: R$ {:.2f}' . format(preco_total_galoes))

print('PREÇO TOTAL: R$ {:.2f}' . format(preco_total_geral))
print()
