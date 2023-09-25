# escreva um programa que faça o computador pensar um numero entra 0 e 5 e faça o usuario descobrir qual foi o numero escolhido pelo computador
# o computador devere escrever na tela se o usuario ganhou ou perdeu

#escolhido = random.choice(comp1)

#import random
#n = int(input('Tente advinhar o número:'))
#num = random.randint(0,5)
#print(num)
#if n == num :
#    print('Parabéns você acertou!')
#else:
#    print('Que pena, você errou!')


import random  
from time import sleep


print('-=-' *20)
print('Rolte da sorte!!!')
print('-=-'*20)
num1 = eval(input('Digite um numero: '))#ATENÇÃO pois usei STR e ele não retornava se era verdadeira caia na condição de falço direto
comp1 = random.randint(1,5)  #funciona direitinho com eval ou int
print('PROCESSANDO...')
sleep(3)
print(f'O numero escolhido foi {comp1}')
if num1==comp1:
    print('Voce ganhou!!!')
else:
    print('Voce perdeu!!!')




