""""
Exemplo 4: Tabuada em Python
"Crie um script em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada"
Primeiro, pedimos qual a tabuada o usuário quer (do 1, do 2, do 3...) e armazenamos essa informação na variável 'tabuada'.
A tabuada nada mais é que multiplicar um número por 1, depois por 2, depois por 3, depois por 4....até chegar no 10.
Vamos fazer com que a variável 'var' receba os valores de uma lista que vai de 1 até 10, e em cada iteração do laço FOR, multiplicamos pelo número que o usuário nos forneceu, a variável 'tabuada'.
Nosso código de tabuada fica assim:
"""
tabuada = int(input("Qual tabuada fazer: ") )

for var in range(1,11):
    print('-=-')
    print(tabuada*var)