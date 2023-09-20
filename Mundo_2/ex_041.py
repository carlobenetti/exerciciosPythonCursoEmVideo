# A confederação Nacional de natação precisa de um programa q leia o ano ne nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: MIRIM;  Ate 14 anos: INFANTIL;  Ate 19 anos: JUNIOR;  Ate 20 anos : SENIOR;  ACIMA: MASTER.
from datetime import date
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
age = ano_atual - ano_nascimento

if age <= 9:
    categoria = 'MIRIM'
elif age <= 14:
    categoria = 'INFANTIL'
elif age <= 19:
    categoria = 'JUNIOR'
elif age <= 20:
    categoria = 'SENIOR'
elif age > 20:
    categoria = 'MASTER'
print(f'Sua categoria é {categoria} pois você possui {age} anos.')

