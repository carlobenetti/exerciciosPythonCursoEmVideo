# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# - Quantas vezes apareceu o valor 9.
# - Em que posição foi digitado o primeiro valor 3.
# - Quais foram os números pares.
# Lembre-se, se um valor não estiver presente. Faça aparecer uma mensagem indicando isso.

valores = []
counter = 0
countNines = 0

# Adicionando os valores a lista
while counter < 4:
    valores.append(int(input("Digite um valor: ")))
    counter += 1
    
# Tranformando a lista em uma tupla
tupla = tuple(valores)

# Resultados        
print(tupla)

# Contando os números noves (9)
countNines = tupla.count(9)
print(f'O número 9 (nove) apareceu {countNines} vezes.')
        
# Encontrando a posição do número 3        
if 3 in tupla:
    print(f'O primeiro três está na posição: {tupla.index(3)+1}.')
else:
    print(f'3 não está na tupla.')



# Separando os valores pares
pares = []

for num in tupla:
    if num % 2 == 0:
        pares.append(num)
print(f'Os valores pares são {num}')














