#crie um programa que leia o nome de uma pessoa independente de quantos sobrenomes ela tenha só mostre o primeiro e o ultimo nome

n=str(input('Digite seu nome: ')).strip()
nome = n.split()
print(f'Muito prazer!!')
print(f'Seu primeiro nome é: {nome[0]} \nE seu ultimo nome é: {nome[-1]}')
#estava fazendo nome(len.nome[-1]) essa forma nao funcionava

