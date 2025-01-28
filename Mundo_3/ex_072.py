# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# - Se digitar um valor fora do intervalo (0 a 20) o programa pede para digitar novamente.
# Ex: - Digite o n° 3.  -->>> Você digitou o número três.
# OBS: Lembre de fazer o exercício usando tuplas.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Digite um número de 0 a 20: "))
    if num >= 0 and num < 20:
        break        
    print('Tente novamente. ', end='')
    

print(f'Você digitou o número: {tupla[num]}')

continuar = int(input('Você quer continuar? Sim [0] ou não [1]: '))

while continuar == 0:
    while True:
        num = int(input("Digite um número de 0 a 20: "))
        if num >= 0 and num < 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número: {tupla[num]}')
    continuar = int(input('Você quer continuar? Sim [0] ou não [1]: '))






