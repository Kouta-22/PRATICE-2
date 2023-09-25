"""
Crie um programa que calcule o reajuste de salario de um funcionario
Caso ele ganha mais que 1200 ele recebe 10% a mais 
Caso ele ganhe menos que 1200 ele recebe 15% a mais 
"""


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

    

"""
salario = eval(input('Digite o salario do funcionario: R$ '))

if salario < 1250:  
    novo = salario * 1.15
else:
    novo = salario * 1.10
print(f'O salario era {salario} com o reajuste do salario  ficou R${novo:.2f}')
"""


