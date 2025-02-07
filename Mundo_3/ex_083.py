# Um programa em que um usuário usa uma expressão qualquer que usa parenteses.
# O aplicativo deverá analisar a expressão passada e ver se os parênteses estão na ordem correta. 


expressao = '(a + b) * c'

stack = []

for charters in expressao:
    if charters == '(':
        stack.append(charters)
    elif charters == ')':
        if stack:
            stack.pop()
        else:
            print(f'Expressão incorreta.')
            break

else:
    if not stack:
        print("Tudo está ok")
    else:
        print(f'Expressão incorreta.')




    