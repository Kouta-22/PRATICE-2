import random
soma = 0 
cont = 0
print('NUMEROS GERADOS')
print('=-'*2)
for c in range(1,7):
    num = random.randint(1,10)
    print(num)
    if num % 2 == 0:
        soma += num
        cont += 1
     
print('=-'*2)# EU ESTAVA ERRANDO POIS COLOCAVA PARA REPETIR COUT E SOMA DENTRO DO LAÇO
print(f'Foram {cont} numeros pares GERADOS')
print(f'A soma dos pares é : {soma}')


