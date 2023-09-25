
#ex do professor

numero = eval(input('Digite um numero: '))
razao = eval(input('Digite a razão: '))
resultado = numero
total = 0
mais = 10
c = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'-> {resultado}',end='')
        resultado += razao
        c += 1
    print(' PAUSA...')
    mais = eval(input('Quantos numeros da PA mais? '))
print(f'forão feitas {c} PA')













