
nota1 = eval(input('Digite uma nota: '))
nota2 = eval(input('Digite uma nota: '))

total = nota1 + nota2
media = total / 2  #OBS: poderia fazer direto usando (NOTA1+NOTA2)/2

if media > 7:
    print(f'A media do aluno foi {media}')
    print('PARABENS, aluno APROVADO')
elif media < 6.9 and media > 5:
    print(f'A media do aluno foi {media}')
    print('CUIDADO, voce esta de RECUPERAÇÃO')
else:
    print(f'A media do aluno foi {media}')
    print('DESAPONTADO, aluno REPROVADO')

