"""
Estrutura de controle aninhada é cosposta por um bloco de comando dentro de outro bloco de comando
Isto é um IF com uma condição extra dentro exemplo 

IF CONDIÇÃO1():
ELIF CONDIÇÃO2():
ELSE:

"""
nome = str(input("Qual o seu nome?  "))
if nome =='Guilherme':
    print('Que nome bonito voce tem!!!')
elif nome == 'gustavo' or nome == 'joao' or nome == 'pedro':
    print('Seu nome é bem popular')
elif nome in 'ana maria paula':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal')

print(f'tenha um bom dia {nome}!!')