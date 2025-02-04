# Crie um programa onde o usuário possa digitar 5 valores numéricos.  
# [] Cadastreos em uma lista já na posição correta sem usar o sort.
# [] Mostre a lista ordenada.


valores = [0, 0, 0, 0, 0]


for item in range(0, 5):
    valorTeste = int(input('Digite um valor: '))
    valores[0] = valorTeste
    


def filtro(valores):
    # Trocando as posições do valor 0:
    if valores[0] > valores[1]:
        valores[0], valores[1] = valores[1], valores[0]
    if valores[0] > valores[2]:
        valores[0], valores[2] = valores[2], valores[0]
    if valores[0] > valores[3]:
        valores[0], valores[3] = valores[3], valores[0]
    if valores[0] > valores[4]:
        valores[0], valores[4] = valores[4], valores[0]
        
    # Trocando as posições do valor 1:
    if valores[1] > valores[2]:
        valores[1], valores[2] = valores[2], valores[1]
    if valores[1] > valores[3]:
        valores[1], valores[3] = valores[3], valores[1]
    if valores[1] > valores[4]:
        valores[1], valores[4] = valores[4], valores[1]

    # Trocando as posições do valor 2:
    if valores[2] > valores[3]:
        valores[2], valores[3] = valores[3], valores[2]
    if valores[2] > valores[4]:
        valores[2], valores[4] = valores[4], valores[2]
    
    # Trocando as posições do valor 3:
    if valores[3] > valores[4]:
        valores[3], valores[4] = valores[4], valores[3]
    
    
    return valores




print(filtro(valores))
    

