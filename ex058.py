import random  

print('-=-' *20)
print('Tente adivinhas no numero que o computador de 0 a 10')
print('-=-'*20)
c = 1
comp1 = random.randint(0,10)

num1 = eval(input('Digite um numero: '))
while num1 != comp1:
    c += 1
    if num1 == comp1:
        print('')
    elif comp1 > num1:
            print('Mais...')
            num1 = eval(input('Voce errou digite novamente um numero: '))#para sair igual o do guanabara basta mudar o INPUT repetindo ele nos if/elif/else:
    else:
            print('Menos...')
            num1 = eval(input('Voce errou digite novamente um numero: '))#para sair igual o do guanabara basta mudar o INPUT repetindo ele nos if/elif/else:

print(f'Voce acertou\nCom o total de {c} tentativas')#para sair igual o do guanabara basta mudar o PRINT repetindo ele nos if/elif/else:






#CODIGO GUNABARA
"""import random
c = 0
comp1 = random.randint(0,10)
print('Tente adivinhar no numero que o computador gerou de 0 a 10')
acertou = False
while not acertou:
    c += 1
    jogador = eval(input('Digite um numero: '))
    if jogador == comp1:#QUANDO JOGADOR FOR IGUAL A COMPUTADOR
        acertou = True#ACERTOU SE TORNA VERDADEIRO SAINDO DO LAÇO WHILE POIS DEIXOU DE SER FALSO
        print('Voce acertou')
    else:
        if jogador > comp1:
            print('Menos...')
        if jogador < comp1:
            print('Mais...')

print(f'Com o total de {c} tentativas')

"""