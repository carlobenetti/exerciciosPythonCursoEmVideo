from datetime import date
usuario = [
    {
    'nome': 'Carlo Benetti',
    'idade': 22,
    'sexo': 'M',
},
    {
    'nome': 'Isabeli',
    'idade': 28,
    'sexo': 'F',
},
    {
    'nome': 'Maria Isabel',
    'idade': 37,
    'sexo': 'F',
},
]


print()


print(f'- Média de idade = {sum(i['idade'] for i in usuario)/len(usuario)}')
print()

print(f'- As mulheres cadastradas foram:')
for mulheres in usuario:
    if mulheres['sexo'] == 'F':
        print(mulheres['nome'] )

print()
print(f'- Pessoas a cima da média:')
for idade in usuario:
    if idade['idade'] > sum(i['idade'] for i in usuario)/len(usuario):
        for k, v in idade.items():
            print(f'{k} = {v};', end=' ')
        print()
print()

print('<< ENCERRADO >>')