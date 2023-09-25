# if e else

#condição simplificada
#tempo = eval(input('Quantos anos tem seu carro?'))
#print('Carro novo' if tempo<=3 else 'carro velho')

#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <=3:
#    print('Seu carro é novo')
#else: 
#    print('Seu carro é velho')
#print('\n fim do programa')
"""
nome = str(input('Qual seu nome?')) #tem que ser usado o comando str 
if nome == 'guilherme':
    print('Que nome lindo voce tem')
else:
    print('Seu nome é tão normal: ')
print(f'Bom dia!{nome}')
"""

n1 = eval(input('Digite a 1° nota: '))
n2 = eval(input('Digite a 2° nota: '))

m = (n1+n2)/2
print(f'sua media foi: {m:.2f}')
if m>=5:
    print(f'Voce passou na media que é: 5')
else:
    print(f'Voce não passou na media que é: 5')







