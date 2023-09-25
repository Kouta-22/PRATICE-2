"""
num1 = eval(input('Digite o primeiro valor: '))
num2 = eval(input('Digite o segundo valor: '))
num3 = eval(input('Digite o terceiro valor: '))
print('^^'*20)
print(f'Os numeros digitados foram {num1} e {num2} e {num3}')
print('^^'*20)
menor = num1
#verificando o menor numero: 
if num2<num1 and num2<num3:   #SE O SEGUNDO NUMERO FOR <MENOR< QUE O PRIMEIRO NUMERO and O SEGUNDO NUMERO FOR <MENOR< QUE O TERCEIRO 
    menor = num2              #O SEGUNDO NUMERO =RECEBE= MENOR 
if num3<num1 and num3<num2:
    maior = num3
#verificando o maior numero
maior = num1 
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3

print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
"""
#TEM COMO FAZER DA MESMA FORMA SÓ QUE USANDO LISTA ONDE VOCE ORDENA (usando o comando sorted) OS VALORES COM BASE NA LISTA
"""
n1 =int(input('digite o primeiro número:  '))
n2 =int(input('Digite o segundo número: '))
n3 =int(input ('Digite o terceiro número: '))

lista =[n1,n2,n3]
lista_ordenada = sorted(lista)

print('O menor número é {}'.format(lista_ordenada[0]))
print ('O maior número é {}'.format(lista_ordenada[2]))
"""


n1 =int(input('digite o primeiro número:  '))
n2 =int(input('Digite o segundo número: '))
n3 =int(input ('Digite o terceiro número: '))

lista =[n1,n2,n3]
lista_ordenada = sorted(lista)

print('O menor número é {}'.format(lista_ordenada[0]))
print ('O maior número é {}'.format(lista_ordenada[-1]))
