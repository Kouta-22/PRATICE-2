
peso = eval(input('Digite seu peso: '))
altura = eval(input('Digite sua altura:'))

imc = peso/(altura * altura)

print(f'Seu imc é de {imc:.2f}')
if imc < 18.5:
    print('Voce esta com MAGREZA!!')
elif imc < 25:
    print('Voce esta com peso IDEAL!!')
elif imc < 30:
    print('Voce esta com SOBREPESO !!')
elif imc < 40:
    print('Voce esta com OBESIDADE!!')
else:
    print('Voce esta com OBSIDADE MORBIDA!!!')



