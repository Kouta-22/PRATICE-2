# Crie um programa que pergunte a distancia de uma viagem em km
# E calcule o preço da passagem cobrando R$ 0,50 por km para viagem de até 200km
# Para viagem mais longas que 200 atribua R$0,45

dist = eval(input('Qual a distancia da sua viagem? '))
print (f'Voce esta preste a começar a viagem de {dist}km')

preço = dist * 0.50 if dist <=200 else dist * 0.45 # VERSÃO SIMPLIFICADA
print(f'O preço da sua passagem sera de {preço}R$') # o preço vai CUSTA 0.50 se for MENOR que 200
                                                    # o preço vai custar 0.45 se a for MAIOR QUE 200

"""
if dist <= 200:
    preço = dist * 0.50
else: 
    preço = dist * 0.45
print(f'E o preço da sua passagem sera de R$ {preço}')
"""


