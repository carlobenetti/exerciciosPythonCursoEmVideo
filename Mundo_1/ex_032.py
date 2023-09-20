# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date # Importando biblioteca que identifica o ano da máquina

ano = int(input('\033[1;32mDigite um ano, ou digite 0 para usar o ano atual: \033[m '))

if ano == 0:
    ano = date.today().year # Aplicando a biblioteca

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    cor = "\033[1;34m"
    print(f'O ano de {ano} {cor}é bissexto\033[m')
else:
    cor = "\033[1;31m"
    print(f'O ano de {ano} {cor}não é bissexto\033[m')