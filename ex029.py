#crie um programa que leia a velocidade de um carro e caso ele exeda o limite de 80km ele recebe multa de 7 $

vel = eval(input('Qual a velocidade do carro: '))

if vel > 80:
    vel = (vel-80)*7
    print('Voce ultrapassou o limite de velocidade')
    print(f'Sua multa é de:\033[7;31;47m{vel} R$\033[m')
print('\033[7;32;44mDirija com cuidado\033[m')