#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida
# Média abaixo de 5.0: REPROVADO
# Media entre 5.0 e 6.9: RECUPERAÇÃO
# Media 7.0 ou superior: APROVADO

#Tabela de cores
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
fim_cor = '\033[m'

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2

if media >= 7:
    print(f'Sua média é: {media:.1f}. \nVocê está {verde}aprovado{fim_cor}.')
elif 7 > media >= 5:
    print(f'A sua média é: {media:.1f}. \nVocê está de {amarelo}recuperação{fim_cor}.')
elif media < 5:
    print(f'Sua média é: {media:.1f}. \nVocê está {vermelho}reprovado.{fim_cor}')