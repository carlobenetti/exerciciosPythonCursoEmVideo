prices = [1299.00, 1299.00, 1349.00, 1329.00, 1199.00, 1259.00, 1179.00, 1299.00]
print(f'\nTamanho da lista: {len(prices)}')

print('\nPreços em ROL: ')
print(sorted(prices))

print('\nMenor preço: ')
print(min(prices))

print('\nMaior preço: ')
print(max(prices))

print('\nMédia preço: ')
print(sum(prices)/len(prices))

print(f'\nModa: {1299.00}')




middle = int(len(prices)/2)-1
middleAfter = int(len(prices)/2)

print(f'Numero 4 e 5 da lista = {prices[middle]} e {prices[middleAfter]}')
print(f'\nMediana: {(prices[middle] + prices[middleAfter])/2}')



# middleBefore = (len(prices)/2)+1