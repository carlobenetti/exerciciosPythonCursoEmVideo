# Crie um programa que leia nome, sexo e idade de várias pessoas
# Guardando os dados de cada pessoa em um dicionário.
# E todos os dicionários em um lista.
# No final mostre:
# [ ] Quantas pessoas foram cadastradas.
# [ ] A média de idade do grupo.
# [ ] Uma lista com todas as mulheres.
# [ ] Uma lista com todas as pessoas com idade acima da média.

pessoa = {}
tabela_pessoas = []


while True:
    
    # Alimentando os dados
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Digite a idade: '))

    # Salvando no dicionário
    tabela_pessoas.append(pessoa.copy())
    
    continuar = str(input('Continuar [s/n]: ')).strip().lower()[0]
    if continuar in 'n':
        break

print()
print(pessoa)

print()
print(tabela_pessoas)

# Mostrando a lista de pessoas
print('-------------')
for linhas in tabela_pessoas:
    for k, v in linhas.items():
        print(k, v)
    print('-------------')




# Resultado

print(f'- Média de idade = {sum(i['idade'] for i in tabela_pessoas)/len(tabela_pessoas)}')
print()

print(f'- As mulheres cadastradas foram:')
for mulheres in tabela_pessoas:
    if mulheres['sexo'] == 'F':
        print(mulheres['nome'] )

print()
print(f'- Pessoas a cima da média:')
for idade in tabela_pessoas:
    if idade['idade'] > sum(i['idade'] for i in tabela_pessoas)/len(tabela_pessoas):
        for k, v in idade.items():
            print(f'{k} = {v};', end=' ')
        print()
print()

print('<< ENCERRADO >>')
















