"""
Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% 
do salário ou então o empréstimo será negado.

"""
valor_imprestimo = float(input("Digite o valor do imprestimo: "))
valor_sal = float(input("Digite o valor do seu salario: "))
valor_anos = int(input("Digite em quantos anos voce ira pagar: "))

prest = valor_imprestimo / (valor_anos * 12) 
valor_minimo = valor_sal * 30 / 100

print(f'Para pagar o valor do imprestimo: R${valor_imprestimo} em {valor_anos} ANOS a prestação sera mensal sera de: R${prest:.2f}')

if valor_minimo >= prest:
    print('Emprestimo CONCEDIDO')
else:
    print('Emprestimo NEGADO')

#primeiro imputar os valores
# segundo criar uma variavel para armazenas o valor das parcelas do emprestimo 
# terceiro o emprestimo vai ser anos X VEZES X 12(doze) dividido pelo valor dos






