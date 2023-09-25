""""
salario = eval(input('Qual é o salario do funcionario: '))
reajuste = salario + (salario *15/100)
print(f'Um funcionario que ganhava R$$ {salario:.2f} com 15% de aumento ganha {reajuste:.2f} ')
"""
# formula de porcentagem de salarial




produto = eval(input('Qual o valor do produto? '))
debito = produto - (produto*10/100)
credito = produto + (produto *8/100)
print(f'O produto custa R${produto:.2f} \nno debito sai a R${debito:.2f} \nno credito a R${credito:.2f}')

desc = produto - debito
jus = produto - credito
print(f'O desconto dado foi de R${desc:.2f} \nO juros foi de {jus:.2f}')


