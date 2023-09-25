"""Para importa uma biblioteca voce pode usar import(biblioteca) para importa a biblioteca toda 
Para usar exclusividade na blibioteca voce usara from/import(bliblioteca/exclusividade)"""

import math
#voce pode formatar uma variavel de acordo com a biblioteca
num = eval(input('Digite um numero: '))
#Com a biblioteca toda importada voce tem que delimitar qual função da biblioteca voce quer usar
raiz = math.sqrt(num)
print(f'A raiz de {num} é = a {math.ceil(raiz)}')


"""
IMPORTAÇÃO EXCLUSIVA
voce tambem pode usar apelido para as importaçoes ex: from math import sqtr AS raizquadrada
from math import sqrt, floor
num = eval(input('Digite um numero: '))
raiz = sqrt(num)
print(f'A raiz de {num} é = a {math.ceil(raiz)}')
"""