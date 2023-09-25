num = eval(input('Digite uma numero: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[34m', end= ' ')
        tot += 1
    else:
        print('\33[31m', end= ' ')
    print(c, end= ' ')
print(f'\nO numero {num} foi dividigo {tot} vezes')
if tot == 2: 
    print('O numero é PRIMO')
else:
    print('O numero NÃO é primo')