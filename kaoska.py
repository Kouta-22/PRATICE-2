"""from tkinter import Y


def fc(x,y):
    s=0
    a = x.lower()
    for i in a:
        if (i==y):
            s = s + 1 
        
    return s
a = 'Aracaju /Sergipe'
x = fc(a,'a')*100
y = fc(a,'e')*10
z = fc(a,'i')
print(x+y+z)"""
"""
nome = input("Entre com seu nome: ")
for letra in nome:
    print(letra)"""

"""nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for letras in nomes:
    print(letras)
"""
"""palavra = input('Entre com uma palavra: ')
print('Digite sair para encerrar o laço: ')
while palavra != 'sair':
    palavra = input(' ')
print('Você digitou sair e agora está fora do laço')"""

while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. ')
    if opcao1 == 'SIM':
        break # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. ')
            if opcao2 == 'SIM':
                break # este break é do segundo laço
            print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')
