dias = eval(input('Quantos dias o carro foi alugado: '))
km = eval(input('Quando km foi rodado: '))
pago = (dias*60) + (km * 0.15)
print(f'O total a pagar é R${pago:.2f} ')
