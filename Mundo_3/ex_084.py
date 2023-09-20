pessoas = []
grupo = []
pessoas_count = 0
pessoas_mais_pesadas = []
pessoas_mais_leves = []
maximo = 0
minimo = 0

while True:
    pessoas.append(str(input('Nome da pessoa = ')))
    pessoas_count += 1
    pessoas.append(int(input('Peso da pessoa = ')))
    grupo.append(pessoas[:])
    pessoas.clear()
    continuar = str(input('Deseja continuar? Sim ou Não = ')).strip()[0]
    if continuar in 'Nn':
        break
        
# Formando uma lista com os pesos
lista_pesos = []
for i in grupo:
    lista_pesos.append(i[1])

# Calculando a média dos pesos:
media_pesos = sum(lista_pesos)/len(lista_pesos)

# Filtrando as pessoas com pesos maiores dos menores
for c in grupo:
    if c[1] >= media_pesos:
        pessoas_mais_pesadas.append(c)
    elif c[1] <= media_pesos:
        pessoas_mais_leves.append(c)
    else:
        break

# Determinando o peso máximo e o peso mínimo
maximo = max(lista_pesos)
minimo = min(lista_pesos)

pessoa_peso_maximo = ''
pessoa_peso_minimo = ''
for e in grupo:
    if e[1] == maximo:
        pessoa_peso_maximo = e[0]
    if e[1] == minimo:
        pessoa_peso_minimo = e[0]
       

# Imprimindo o resultado
print('\n')
print(30*'-')
print(f'{9*" "} Informações')
print(30*'-')

print(f'\nForam cadastradas {pessoas_count} pessoas.')

print(f'\nA média dos pesos é {media_pesos:.2f}')

print(f'\nA pessoa mais pesada é {pessoa_peso_maximo} com {maximo} Kg.')
print(f'A pessoa mais leve é {pessoa_peso_minimo} com {minimo} Kg.')

print(f'\nAs pessoas mais pesadas são: ')
for pessoa in pessoas_mais_pesadas:
    print('-', pessoa[0], 5*'..', pessoa[1], 'kg')
print(f'\nAs pessoas mais leves são: ')
for pessoa_leve in pessoas_mais_leves:
    print('-', pessoa_leve[0], 5*'..', pessoa_leve[1], 'kg')

    