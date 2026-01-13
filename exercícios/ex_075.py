# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# - Quantas vezes apareceu o valor 9.
# - Em que posição foi digitado o primeiro valor 3.
# - Quais foram os números pares.
# Lembre-se, se um valor não estiver presente. Faça aparecer uma mensagem indicando isso.

numero = (int(input('Digite um número:')), 
          int(input('Digite um número:')), 
          int(input('Digite um número:')), 
          int(input('Digite um número:')))

print(' ')
print(f'Valores digitados: {numero}')

#Vezes em que o 9 apareceu
print(f'O valor 9 apareceu {numero.count(9)} vezes.')

# Primeiva vez que apareceu o 3
if 3 in numero:
    print(f'O valor 3 apareceu na posição: {numero.index(3)+1}')
else:
    print(f'O valor 3 não está na lista.')
    
#Números pares
print('Os valores pares são:')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
        
        
    
    

        











