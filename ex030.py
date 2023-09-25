#cri um programa que leia um numero inteiro e informe se ele é par ou impar 

num = eval(input('Me diga um numero qualquer: '))
resultado = num %2

if resultado == 1:
    print (f'O resultado foi \033[4;31;40mImpar\033[m')
else:
    print('O resultado foi \033[4;36;40mPar\033[m')
