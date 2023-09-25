maior = 0 
menor = 0

for c in range(1,4):
    peso = eval(input(f'Digite o {c}° peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:

        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
        
print(f'O maior peso é de {maior}Kg e O menor é de {menor}Kg')



