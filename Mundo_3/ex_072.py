# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# - Se digitar um valor fora do intervalo (0 a 20) o programa pede para digitar novamente.
# Ex: - Digite o n° 3.  -->>> Você digitou o número três.
# OBS: Lembre de fazer o exercício usando tuplas.



tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


userNumber = int(input('Digite um número de 0 a 20: '))


# Controle de saida
while userNumber < 0 or userNumber > 20:
    print('Número fora do intervalo, digite novamente: ')
    userNumber = int(input('Digite um número de 0 a 20: '))
    if userNumber > 0 or userNumber < 20:
        break





pos = userNumber
print(f"Você digitou o número {tupla[pos]} (ou seja {userNumber})")



# Controle de saida
keep = int(input("""
Aperte 0 para continuar.
Aperte 1 para sair.
"""))

while keep > 1 or keep < 0:
    print('Número fora do intervalo, vamos novamente...')
    keep = int(input("""
    Aperte 0 para continuar.
    Aperte 1 para sair.
    """))
    if keep == 0 or 1:
        break



if keep == 0:
    userNumber = int(input('Digite um número de 0 a 20: '))
    while userNumber < 0 or userNumber > 20:
        print('Número fora do intervalo, digite novamente: ')
        userNumber = int(input('Digite um número de 0 a 20: '))
        if userNumber > 0 or userNumber < 20:
            for pos, i in enumerate(tupla):
                pos = userNumber            
    print(f"Você digitou o número {tupla[pos]} (ou seja {userNumber})")
else:
    print("O programa terminou.")



            
            
        





















