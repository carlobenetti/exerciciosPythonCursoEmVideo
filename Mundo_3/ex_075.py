#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla
#No final, mostre:;
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


lista = []
# Recebendo os números e transformando em tupla
for c in range(0, 4):
    num = int(input('Type a number: '))
    lista.append(num)
lista = tuple(lista)
print(lista)

# Identificando os nums pares
par = []
for c in lista:
    if (c%2) == 0:
       par.append(c)


print(f'O valor 9 apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O primeiro valor 3 está na posição {lista.index(3)+1}')
print(f'Os números pares foram {par}')

 