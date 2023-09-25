soma = 0 
cont = 0
for c in range(0,501,3):
    if c % 2 == 1:
        cont += 1
        soma += c 

print(f'A soma dos {cont} Numeros são {soma}')

