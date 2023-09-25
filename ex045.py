import random
from time import sleep
num = random.randint(1,3)
print('''Jo-Ken-Po
Escolha:
[1] = PEDRA
[2] = PAPEL
[3] = TESOURA ''')
jogar = eval(input('Escolha uma: '))
print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('PO!')
sleep(1)
if jogar == 1:
    print('Voce escolheu PEDRA')
    if jogar == num:
        print('EMPATE!')
    elif num == 2:
            print('O computador escolheu PAPEL voce perdeu!!!')
    elif num == 3:
                print('Voce ganhou o computador escolheu TESOURA!!!')
elif jogar == 2:
    print('Voce escolheu PAPEL')
    if jogar == num:
        print('EMPATE!')
    elif num == 3:
            print('O computador escolheu TESOURA voce perdeu!!!')
    elif num == 1:
                print('Voce ganhou o computador escolheu PEDRA!!!')
elif jogar == 3:
    print('Voce escolheu TESOURA')
    if jogar == num:
        print('EMPATE!')
    elif num == 1:
            print('O computadpr escolheu PEDRA voce perdeu!!!')
    elif num == 2:
                print('Voce ganhou computador escolheu PAPEL!!!')
else:
    print('OPÇÂO INVALIDA')





