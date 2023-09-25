num = eval(input('Primeiro termo:  '))
razao = eval(input('Razão da PA '))

resultado = num#estava colocando isso dentro do while e dava erro
#resultado = 0
c = 1
print(f'{num}-> ',end ='')
while c <= 11:
    
    resultado = resultado + razao 
    #resultado + num 
    
    if c < 11:
        print(f'{resultado}', end='-> ')
    c += 1