# Um programa em que um usuário usa uma expressão qualquer que usa parenteses.
# O aplicativo deverá analisar a expressão passada e ver se os parênteses estão na ordem correta. 

expr = str(input('Digite a expressão: '))
pilha = []

for items in expr:
    if items == '(':
        pilha.append('(')
    if items == ')':
        if len(pilha) > 0:
            pilha.pop() # Remove o ultimo item da pilha
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'A expressão está correta.')
if len(pilha) != 0:
    print(f'A expressão está incorreta.')  