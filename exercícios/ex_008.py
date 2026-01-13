#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
v1 = float(input('Type the meters:'))
print(f'The value in kilometers is: {v1/1000}km \nThe value in hectameters is: {v1/100}hm')
print(f'The value in decameters is: {v1/10}dam \nThe value in decimeters is: {v1*10}dm')
print(f'The value in centimeters is: {v1*100}cm \nThe value in millimeters is: {v1*1000}mm')
