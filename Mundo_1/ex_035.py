# Leia um programa de três retas e diga ao usuário se elas formam um triângulo

"""Cores"""
amarelo = "\033[1;33m"
verde = "\033[1;32m"
vermelho = "\033[1;31m"
corfim = "\033[m"

"""Mensagem de pergunta"""
print(f'{amarelo}{11 * "-=-"}{corfim}')
print(f'{5 * " "}{amarelo}"Teste dos triângulos"{corfim}')
print(f'{amarelo}{11 * "-=-"}{corfim}')
print(f'{verde}Digite 3 segmentos de triângulo:{corfim}')
s1 = float(input('Segmento 1: '))
s2 = float(input('Segmento 2: '))
s3 = float(input('Segmento 3: '))

"""Cálculo do triangulo"""
if s1 + s2 >= s3 and s1 + s3 >= s2 and s2 + s3 >= s1:
    print(f'Os segmentos {verde}formam{corfim} um triângulo.')
else:
    print(f'Os segmentos {vermelho}não formam{corfim} um triângulo.')
    