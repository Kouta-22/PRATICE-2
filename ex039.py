from datetime import date

nasc = eval(input('Qual o ano de seu nascimento: '))
atual = date.today().year
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos EM {atual}')

if idade == 18:
    print('Esta na hora na hora de se alistar!!!')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo 
    print(f'Voce já deveria ter se alistado a {saldo} anos !!!')
    print(f'Voce deveria ter se alistado em {ano} ')
else:
    saldo = 18 - idade
    ano = atual + saldo
    print(f"Ainda não chegou a hora de se alistar falta {saldo} anos !!!")
    print(f'Seu alistado sera em {ano} ')
