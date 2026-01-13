#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('\033[1;30;46m Digite seu salário em reais: \033[m  '))

aumento = salario*(15/100)

print(f'Seu salário é de {salario} R$'
      f'\nVocê recebeu um aumento de {aumento} R$'
      f'\nAgora seu salário é de {salario+aumento} R$')

