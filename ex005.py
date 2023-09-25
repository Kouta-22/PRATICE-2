print('Bom dia, deseja calcular a media do aluno? ')

n = eval(input('\nDigite a primeira nota aqui: '))
n1 = eval(input('Digite a segunda nota aqui: '))
n2 = eval(input('Digite a terceira nota aqui: '))
m= (n+n1+n2)/3

print(f'A primeira nota é {n} e a segunda é {n1} a terceira nota é {n2} a media do aluno é  {m:.2f}')
print(type(m))

