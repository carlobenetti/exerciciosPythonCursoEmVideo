# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
palavra = input('\033[1;30;107mDigite algo: \033[m')

if palavra.isalnum() == True: #Palavras alfanuméricas são (space)!#%&? etc.
    print(f'A palavra {palavra} é alfanumérica')
else:
    print(f'A palavra {palavra} não é alfanumérica')

if palavra.isalpha() == True: #Retorna True se todas as palavras estão no alfabeto
    print(f'A palavra {palavra} está no alfabeto')
else:
    print(f'A palavra {palavra} não está no alfabeto')

if palavra.isascii() == True: # Retorna True se todos os caracteres na string forem caracteres ascii
    print(f'A palavra {palavra} é um caractere ascii')
else:
    print(f'A palavra {palavra} não é um caractere ascii')

if palavra.isdigit() == True: # Retorna True se todos os caracteres na string forem dígitos
    print(f'A palavra {palavra} é um digito')
else:
    print(f'A palavra {palavra} não é um digito')

if palavra.isidentifier() == True: # Uma string é considerada um identificador válido se contiver apenas letras
    # alfanuméricas (a-z) e (0-9) ou sublinhados (_).
    # Um identificador válido não pode começar com um número ou conter espaços.
    print(f'A palavra {palavra} é um identificador válido')
else:
    print(f'A palavra {palavra} não é identificador válido')

if palavra.isdecimal() == True: # Decimais são os 1ºs nºs pós vírgula EX: 1,2 (2 é decimal), porém aqui em 12, 10 é a
    # decimal
    print(f'A palavra {palavra} é decimal')
else:
    print(f'A palavra {palavra} não é decimal')

if palavra.islower() == True:
    print(f'A palavra {palavra} é toda minuscula')
else:
    print(f'A palavra {palavra} não é toda minúscula')

if palavra.isupper() == True:
    print(f'A palavra {palavra} é toda maiúsucula')
else:
    print(f'A palavra {palavra} não é toda maiúsucula')

if palavra.isnumeric() == True: # retorna Verdadeiro se todos os caracteres forem numéricos (0-9), ² e ¾.
    print(f'A palavra {palavra} é numérica')
else:
    print(f'A palavra {palavra} não é numérica')

if palavra.isprintable() == True:
    print(f'A string {palavra} é printável')
else:
    print(f'A string {palavra} não é printável')

if palavra.isspace() == True: # Retorna True se todos os caracteres forem espaços em branco EX: "    "
    print(f'A string {palavra} são apenas espaços em branco')
else:
    print(f'A string {palavra} não são apenas espaços em branco')

if palavra.istitle() == True: # Retorna Verdadeiro se todas as palavras em um texto começam com uma letra maiúscula,
# e o resto da palavra são letras minúsculas. Símbolos e números são ignorados. EX: Olá Mundo Meu
    print(f'A string {palavra} segue as regras de um título')
else:
    print(f'A string {palavra} não segue as regras de um título')
