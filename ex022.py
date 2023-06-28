#fatiamento de strings
#apenas uma 1 casa apois o valor maximo
# fatiamento com condição ex: [9:21:2] 9 e 21 é o delimetro da string já o 2 é a condição que é de 2 em 2 casas 

# C u r s o  E m  V i d e o  P y t h o n
# 0 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 2  

#frase = 'Curso em video python'
#print(frase[9:21:2])

#frase = 'curso em video python'
#print(frase[:5]) # ele vai rodar da casa inicial até a casa 5 lembrando que inicia em 0
#caso voce use [15:] ela começa da casa 15 e corre ate o final da string 
#frase = 'Curso em video Python'
#print(frase[9::3])# nesse caso ele começa do 9 :: percorre  o codigo todo pulando de 3 em 3 

#função len = ler os espaços na memoria que estao sendo utilizado len(frase)
#função .count('x') ele sinaliza quantas vezes foi utilizado a string que esta no ('x')  tambem pode se usar delimitador nele ex: ('x,0,13')
#função .find('xxx') ele sinaliza em que momento começou a string ('xxx') obs caso o resultado da busca seja -1 significa que não existe uma string xxx
#função in 'xxx' retorna se existe com o valor True ou False
#função .replace('xxxx','yyyy') ele substitui 'xxx' em 'yyy' 
#função .UPPER() e .LOWER()   ele joga todas as letras para maiusculo e em minusculo
#função .capitalize() ele joga a primeia letra da string para maiusculo e deixas todas as outras em minusculo
#função .title() já o capitalize ele joga toda as letras que for seguidas de ESPAÇO em maiusculas
#função .strip() ele remove os espaços em branco antes do inicio da string e no final da string ex: ----gui dias---- removendo os ----
#função .Rstrip e Lstrip Rstrip retira os espaços da direita e Lstrip eos da esquerda
#função .split() ela basicamente separa uma string em uma nova string com base no espaço
#função '-'.join() ela basicamente junta varias strings em uma só acrescentando um espaço entra as strings
#EXEMPLOS
#frase = 'Curso-e-Video-Python'
#print("""Com o uso de 3 aspas voce pode digitar textos longos
# por exemplo que contenham mais de uma linha """)

#frase = 'Curso em Video Python       '
#print(len(frase)) ele contabiliza até os espaços digitados
#frase = 'curso em video python'
#print (frase.replace('python','andoird'))  # uma string em seus micro elemnetos são imutaveis 
                                            # para mudar uma string vc teria que atribuir o resultado da mudança para a viriavel
#frase = "curso em video"
#print('curso' in frase) # o retorno é true

#frase = 'curso em video python '
#print(frase.find('video')) # aqui ele busca a posição que a str video esta apartir do seu 1 caractere// caso não encontre retorna -1


#frase = 'curso em Video Python'
#print(frase.lower().find('video')) #desse jeito ele transforma tudo em minusculo e depois efetua a busca da string


#crie um programa que leia o nome completo de uma pessoa e mostre: 
# A) O nome com todas as letras maiusculas
# B) O nome com todas as letras Minusculas 
# C) Quantas letras ao todo sem os espaços
# D) Quantas letras tem o 1 nome


frase = str(input('Digite seu nome: ')).strip()
print(f'Seu nome em maiusculo fica: {frase.upper()}')
print(f'Seu nome em minuculo fica: {frase.lower()}')
print(f'Seu nome tem {len(frase)-frase.count(" ")} letras.')#obs não pode usar duas aspas simples no inicio/fim e no meio do codigo 
#print(f'Sey primeiro nome tem {frase.find(" ")}')

print(f'Seu primeiro nome tem {frase.split()[0]} e tem {len(frase.split()[0])}')




