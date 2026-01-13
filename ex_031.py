# Pergunte a distãncia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens
# de até 200 Km e R$ 0,45 para viagens mais longas.
kilometros = int(input('Quantos km foram percorridos: '))

if kilometros <= 200:
    cor = "\033[1;34m"
    print(f'A passagem custa {cor}{kilometros*0.50} R$\033[m')
else:
    cor = "\033[1;31"
    print(f'A passagem custa {cor}{kilometros*0,45} R$\033[m')
print(f'Obrigado por comprar {cor}(❁´◡`❁)\033[m')

