# faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno, e tangente desse angulo
import math
an = eval(input('digite um angulo: '))
seno = math.sin(math.radians(an))
print(f'O angulo de {an} tem o SENO de : {seno:.2f}')
coss = math.cos(math.radians(an))
print(f'O angulo de {an} tem o COSSENO DE {coss:.2f}')
tan= math.tan(math.radians(an))
print (f'O angulo de {an} tem a TANGENTE DE: {tan:.2f}')

