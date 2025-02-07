# Um programa onde o usuário possa digitar vários valores numéricos.
# [] Cadastre-os em uma lista.
# [] Se o número já exista lá dentro, ele não será adicionado.
# [] No final, serão exibidos todos os valores únios digitados, em ordem crescente.



numeros = list()

while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado.')


    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
    
    numeros.sort()
    print(numeros)

print(numeros)



