'''
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
tamanho_arquivo = float(input('Qual o tamanho do arquivo para download (em Mb)? '))
velocidade_internet = int(input('Qual a velocidade do link de Internet (em Mbps)? '))

tempo_download = (tamanho_arquivo / velocidade_internet) / 60
minutos = int(tempo_download)
segundos = round((tempo_download % 1) * 60)
print('Tempo aproximado de download do arquivo usando este link (em minutos): {}m{}' . format(minutos, segundos))