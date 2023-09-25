from datetime import date


atual =  date.today().year

maior = 0
menor = 0
for c in range(1,5):
    nasc = eval(input(f'Digite o {c}° ano de nascimento: '))#o {c} acrescenta mais 1 automaticamente
    idade = atual - nasc # para extrair a maioridade( idade recebe o ano atual que foi importado menos o nascimento imputado  )
    if idade > 18:# condição para saber se entra no IF ou ELSE
        maior += 1 # se entra no IF soma mais 1
    else:  
        menor += 1 # se entrar no ELSE soma mais 1 
print(f'Ao todo tivemos {maior} pessoas maiores de idade') # imprimir a quantidade de vez que ele passou pela condição do IF: maior += 1
print(f'E tambem {menor} menor de idade') # Iprimiri a quantidade de vez que ele passou pelo ELSE: menor += 1 







