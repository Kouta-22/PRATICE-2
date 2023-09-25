#crie um programa que crie um lista e leia em ordem aleatoria
import random

n1=str(input('O primeiro aluno: '))
n2=str(input('O segundo aluno: '))
n3=str(input('O terceiro aluno: '))
n4=str(input('O quarto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação sera:  ')
print(lista)

