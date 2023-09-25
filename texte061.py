numero = eval(input('Digite um numero para PA: '))
razao = eval(input('Digite a razão da PA: '))
print('=-'*7)
c = 0
resultado = numero 
print(numero,end=' ')
while c < 9:
    resultado = resultado + razao
    print(f' -> {resultado}',end='')
    c += 1

