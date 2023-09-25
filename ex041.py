from datetime import date


nasc = eval(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print(f'Sua caregoria é MIRIM pois voce só tem {idade}')
elif idade <= 14:
    print(f'Sua categoria é INFANTIL pos voce tem {idade} anos')
elif idade <= 19:
    print(f'Sua categoria é JUNIOR pois voce tem {idade} anos')
elif idade <= 25:
    print(f'Sua categoria é SENIOR pois voce tem {idade} anos')
else: 
    print(f'Sua categoria é MASTER pois voce tem {idade} anos')





