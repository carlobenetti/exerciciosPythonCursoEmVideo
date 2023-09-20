#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a sua nota: '))
nota2 = float(input('Digite a sua nota: '))
media = (nota1+nota2) / 2

if media >= 7:
    cor = '\033[1;30;42m'
    resultado = 'Você passou!!!'
else:
    cor = '\033[1;30;41m'
    resultado = 'Você não passou.'
print(f'A sua média é {cor}{media}\033[m, {resultado}')

