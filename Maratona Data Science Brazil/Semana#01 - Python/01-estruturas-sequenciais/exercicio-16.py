'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
qtde_lata_tinta = 18
preco_lata_tinta = 80
cobertura_lata_tinta = qtde_lata_tinta * 3
qtde_latas_necessarias = 0
preco_total = 0.00

tamanho_area = float(input('Qual o tamanho da área a ser pintada em m2? '))

if tamanho_area <= cobertura_lata_tinta:
    qtde_latas_necessarias = 1
else:
    qtde_latas_necessarias = int(tamanho_area / cobertura_lata_tinta)
    if (tamanho_area % cobertura_lata_tinta > 0):
        qtde_latas_necessarias += 1

preco_total = qtde_latas_necessarias * preco_lata_tinta

print('Quantidade de latas necessárias:', str(qtde_latas_necessarias))
print('Preço total: R$ {:.2f}' . format(preco_total))

