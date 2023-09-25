print('============Loja do Kouta==============')
preço = eval(input('Digite o valor total das compras: '))
forma = eval(input('''Qual a forma de pagamento?
[1] à vista dinheiro/cheque
[2] à vista no cartão de debito
[3] 2x parcelada no cartão
[4] 3x ou mais parcelada no cartão
Qual é a opção de pagamento: '''))
credito0 = preço - (preço*10/100)
credito1 = preço - (preço*5/100)
credito2 = preço + (preço*20/100)
desc0 = preço - credito0
desc1 = preço - credito1
desc2 = preço - credito2
if forma == 1: 
    print(f'O valor das compras receberão desconto de {desc0}R$\nE o valor final ficará: {credito0}R$')
elif forma == 2:
    print(f'O valor das compras receberão o desconto de {desc1}R$\nE o valor final ficará {credito1}R$')
elif forma == 3: 
    parcela = preço / 2
    print(f'O valor das compras ficará : {preço}R$')
    print(f'E suas parcelas custarão {parcela}R$ cada')
else:
    parcela = eval(input('Quanstas parcelas sera: '))
    parcela = credito2 / parcela
    print(f'O valor das compras ficará: {credito2}R$')
    print(f'E suas parcelas custarão {parcela}R$ cada')


    


