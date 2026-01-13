#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angle = float(input('Type an angle: '))
sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))
print(f'seno= {sen:.2f}\ncosseno= {cos:.2f}\ntangente= {tan:.2f}.')