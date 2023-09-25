salario = eval(input('Digite o salario do funcionario: R$ '))


if salario > 1250:  
    salmais = salario + (salario * 10/100)
    jusmais = salmais - salario 
    print(f'O salario inicial era de R${salario}' )
    print(f'Com o reajuste do salario de 10% ficou R${salmais:.2f}')
    print(f'O total do reajuste foi de: R${jusmais:.2f}')
else:#estava usando 2 if funciona tambem
    salmenos = salario + (salario * 15/100)
    jusmenos = salmenos - salario
    print(f'O salario inicial era de R${salario}')
    print(f'Com o reajuste do salario de 15% ficou R${salmenos:.2f}')
    print(f'O total do reajuste foi de: R${jusmenos:.2f}')