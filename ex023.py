#faça um programa que leia numeros de 0 a 9999 e mostre na tela cada digito separo em unidade, dezena, centena e milhar
"""
num = int(input('Digite um numero: '))
n = str(num)
print(f'O numero analisado: {num} ')
print(f'Unidade: {n[3]}')
print(f'dezena: {n[2]}')
print(f'centena: {n[1]}')
print(f'milhar: {n[0]}')
"""
#OUTRA FORMA 

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print (f'Analisando o numero: {num}')
print(f'A Unidade é: {u}')
print(f'A dezena  é: {d}')
print(f'A centena é: {c}')
print(f'O milhar é : {m} ')
