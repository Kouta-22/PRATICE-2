maior_idade = 0
media = 0
cont = 0
contf = 0
nome_mais_velho = ''

for c in range(1,4):
    print('-='*5, end=' ')
    print(f'{c}º PESSOA',end=' ')
    print('-='*5)
    nome = str(input('Digite o nome:  ')).strip()
    idade = eval(input('Digite a idade: '))
    sexo = str(input('Qual sexo [M/F]:  ')).upper()
    cont += idade# variavel contadora para calcular a media
        #PASSO 1
    if c == 1 and sexo in 'Mm': # SE contador(c) == 1 e sexo entre 'Mm': faça
        maior_idade = idade# Maior_idade =RECEBE= idade
        nome_mais_velho = nome# nome_mais_velho =RECEBE= nome
        #PASSO 2
    elif sexo in 'Mm' and idade > maior_idade:# SE sexo in 'Mm'  E idade MAIOR QUE maior_idade 
        maior_idade = idade # a maior_idade =RECEBE= idade
        nome_mais_velho = nome# Nome_mais_velho =RECEBE= nome

    elif sexo in 'Ff' and idade < 18:
        contf += 1#contador feminino com base na quantidade que apareceu Ff e forão menor que 18

media = cont/c#calculo da media
print(f'A media de idade do grupo é: {media:.0f} ANOS')
print(f'O homem mais velho é {nome_mais_velho} e tem {maior_idade} anos')#Imprimir NOME_MAIS_VELHO e MAIOR_IDADE// OBS: eles receberão os maiores valor no 2 PASSO
print(f'Existe {contf} mulheres menor de idade')#imprimir quantas vezes foram contadas o sexo feminino menor de idade

