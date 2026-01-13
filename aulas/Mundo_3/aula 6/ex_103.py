# Um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# O nome do jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gols='<desconhecido>'):
    # Pegando as informações do jogador
    nome = str(input('Nome do jogador: '))
    gols = str(input('Número de gols: '))
    if nome.strip() == '':
        ficha(gols=gols)
    else:
        ficha(nome, gols)
    
    
    print(f'O jogador {jog} fez {gols} gols(s) no campeonato.')


ficha()
    