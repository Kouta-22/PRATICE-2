""" faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
calcule e mostre o comprimento da hipotenusa"""
co=eval(input('Comprimento do cateto oposto: '))
ca=eval(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2) # esse calculo pode ser feito com a importação da biblioteca math com a função .hypot/ ex: hi = math.hypot(co,ca)
print(f'A hipotenusa vai medir {hi:.2f}')

