numero = eval(input('Digite um termo para PA: '))
razao = eval(input('Digite a razão da PA: '))
resultado = numero
c = 1 
novos = 1
total = 0
print(numero, end=' ')



while c <= 9:
    resultado = resultado + razao
    print(f' -> {resultado}',end='')
    if c == 9:
        print(' Pausa...')
        novos = eval(input('Deseja calcular mais? '))
        while novos != 0:
            resultado = resultado + razao
            print(f'-> {resultado}',end='')
            novos -= 1
    c += 1
    
    
    
    
    
    
    
    
   









