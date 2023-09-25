from time import sleep

num1 = eval(input('Digite o primeiro valor: '))
num2 = eval(input('Digite o segundo valor: '))
resultado = eval#variavel de controle pois usando opção rebendo 'resultado' de opção pode dar erro no codigo
#erro onde caso opção de um valor do menu ele entrava na opção do menu

menu = False

while menu != True:


    opção = eval(input('''
[1] Somar
[2] Multiplicar
[3] Maior 
[4] Novos numeros
[5] Sair

Digite uma opção: '''))

    if opção == 1:
        resultado = num1 + num2

        print(f'\nO resultado de {num1} + {num2} = {resultado}')
    if opção == 2:
        resultado = num1 * num2

        print(f'\nO resultado de {num1} X {num2} = {resultado}')
    if opção == 3:    
        if num1 > num2:

            print(f'\nO maior numero é: {num1}')
        else:
            print(f'\nO maior é {num2}')
    if opção == 4:
        num1 = eval(input('Digite novos numeros: '))
        num2 = eval(input('Digite novos numeros: '))
    if opção == 5:
        menu = True
        print('Finalizando...')
    if opção > 5:
        print('Opção invalida digite novamente!')
    sleep(1)
print('=='*5,'FIM DO PROGRAMA','=='*5)

