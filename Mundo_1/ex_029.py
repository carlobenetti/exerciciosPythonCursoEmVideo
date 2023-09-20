#Ler a velocidade de um carro, se ultrapassar 80km/h print("Você foi multado"),
# multa de 7 reais por cada 1km acima do limite
speed = int(input('Digite a velocidade do carro: '))

if speed < 80:
    print(f'Sua velocidade é {speed} < 80')
else:
    print(f'Voce foi multado em {((speed - 80)*7):.2f} Reais. \nPreste mais atenção por gentilesa seu idiota!!!')
    