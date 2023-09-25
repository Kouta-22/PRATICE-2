#RESOLUÇÃO 1 com importação
"""from math import factorial

num1 = eval(input('Digite um valor calcular o fatorial: '))
fac = factorial(num1)
print(f'O fatorial de {num1} é {fac}')"""

num = eval(input('Digite um numero: '))

c = num
f = 1  # o fator nulo de multiplicação é 1
print(f'Calculando o fatorial de {num} != ',end='')
for c in range(num,0,-1):#condição decrecente de num até 0 faça
    print(f'{c} ', end='')#print 'c' variavel de controle 
    print('X 'if c > 1 else '= ', end='')# print personalizado enquanto c for maior que 1 print X // else(senão) print =
    f = f * c# O calculo de fatorial é dado por fatorial * c (contador que esta indo na ordem decrecente)

print(f'{f}',end='')
































