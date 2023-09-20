# Crie um programa onde o usuário pode digitar vários valores
# numéricos e depois cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# Exiba todos os valores únicos digitados em ordem crescente.

valores = []

while True:
    val = int(input('Digite um valor? '))
    # Se o valor não estiver na lista, adicione a ela.
    if val not in valores:
        valores.append(val)
    continuar = str(input('Continuar sim ou não? ')).strip().upper()[0]
    if continuar in 'N':
        break

valores.sort()
print(f'\n{"-"*30}')
print(valores)
