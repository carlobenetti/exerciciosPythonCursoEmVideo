# Pergunte o salário, printe o valor do seu aumento.
# Salários superiores a 1.250,00R$, printe um aumento de 10%
# Para inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o seu salário: '))
print(f'Seu salário é de {salario}')

if salario <= 1250:
    aumento = (salario*15)/100
    print(f'Você recebeu um aumento de {aumento}, seu novo salário é de {salario+aumento}R$')
else:
    aumento = (salario*10)/100
    print(f'Você recebeu um aumento de {aumento}, seu novo salário é de {salario+aumento}R$')

    