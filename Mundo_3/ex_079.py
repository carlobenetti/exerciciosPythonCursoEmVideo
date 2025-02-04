# Um programa onde o usuário possa digitar vários valores numéricos.
# [X] Cadastre-os em uma lista.
# [X] Se o número já exista lá dentro, ele não será adicionado.
# [X] No final, serão exibidos todos os valores únios digitados, em ordem crescente.


valores = []
counter = 'S'
novoValor = 0

# Adicionando os valores a lista.
while counter == 'S':
    novoValor = int(input('Digite um valor: '))
    if novoValor not in valores:
        valores.append(novoValor)
    
    counter = str(input('Quer continuar? [S/N]: '))[0].upper() #Remover os espaços extras que alguem pode adicionar.
    
    
print(f'Os valores da sua lista em ordem crescente foram: {sorted(valores)}')
    
    