num = eval(input('Digite um numero: '))
print('''escolha uma das bases para conversão
[1] Converter em Binario: 
[2] Converter em Octal: 
[3] Converter em Hexadecimal: ''')
opção = eval(input('Sua opção: '))
if opção == 1:
    print(f'\033[7;31;44m{num}\033[m Convertido para Binario é = \033[7;31;44m{bin (num)[2:]}\033[m ')#lembrar de por [2:] pois por padrão o python escreve a sigla antes
elif opção == 2:
    print(f'\033[7;31;44m{num}\033[m Convertido para Octal é = \033[7;31;44m{oct(num)[2:]}\033[m')#lembrar de por [2:] pois por padrão o python escreve a sigla antes
elif opção == 3: 
    print(f'\033[7;31;44m{num}\033[m Convertido para Hexadecimal é = \033[7;31;44m{hex(num)[2:]}\033[m')#lembrar de por [2:] pois por padrão o python escreve a sigla antes
else:
    print('Opção invalida >:[')

