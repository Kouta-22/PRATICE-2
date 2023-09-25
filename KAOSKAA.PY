#s = 0
#a = 1
#while s < 5:
#    s = 3*a
#    a += 1
#    print(s)

"""Ao ser testada pela primeira vez, a condição do while é verdadeira, já que s vale zero. 
Assim, a variável s recebe o valor 3 (3x1) e a variável a é acrescida de uma unidade, ficando com o valor 2.
 Em seguida, é impresso o valor de s (3). A condição do while é, então, testada novamente, sendo mais uma vez verdadeira, porque s tem o valor 3 
(menor que 5). Nessa iteração, a variável s recebe o valor 6 (3x2) e a variável a é acrescida de uma unidade, ficando com o valor 3. Em seguida,
é impresso o valor de s (6). A condição do while é, então, testada novamente e é falsa,
já que s tem o valor 6, maior que 5. Com isso, o laço while é encerrado e nada mais é impresso. Logo, foram impressos os valores 3 e 6."""
"""
escolha = input("Escolha uma opção de função: 1 ou 2: ")
if escolha == '1':
    def func1(x):
        return x + 1
else:
    def func2(x):
        return x + 2

s = func1(10)
print(s)"""



#def taximetro(distancia, multiplicador=1):
 #   largada = 3
  #  km_rodado = 2
   # valor = (largada + distancia * km_rodado) * multiplicador
   # return valor

#pagamento = taximetro(3.5)
#print(pagamento)



"""
  1 def taximetro(distancia)::
  2 def calculaMult():
  3 if distancia < 5:
  4 return 1.2
  5 else:
  6 return 1
  7 multiplicador = calculaMult()
  8 largada = 3   
  9 km_rodado = 2
10 valor = (largada + distancia * km_rodado) * multiplicador
11 return valor
12
13
14 dist = eval(input("Entre com a distancia a ser percorrida em km: "))
15 pagamento = taximetro(dist)
16 print(f'O valor a pagar é R$ {pagamento}')
"""
"""
from cgitb import text
from tkinter import Label, Tk


def msg_pers(msg,titulo,segundos):
    janela = Tk()
    janela.title(titulo)
    Label(janela,text=msg).pack()
    janela.after(segundos *1000, janela.destroy)#o after trata em milissegundo 
    janela.mainloop()
#chamamento de função
msg_pers('Bom dia, Guilherme!','Boas vindas',3)
"""
"""
from tkinter import Tk
from tkinter.filedialog import askdirectory

def escolha_diretorio():
    janela = Tk
    janela.withdraw()
    diretorio = askdirectory
    return diretorio
diretorio = escolha_diretorio
"""
"""
def fun1(texto):
    corrigir = ' '.join(texto.split())
    return corrigir

texto = fun1 ('  guilherme dias    coelho     ')
print(texto)

"""
"""
from tkinter import Label, Tk
from os import system
system('cls')

def tela_inicial():
    janela = Tk()
    janela.title('Programa')#nota eu tentei usar o titulo depois do mainloop e não exibia o titulo programa
    largura = 400
    altura = 60 
    janela.geometry(f'{largura}x{altura}')
    Label(janela, text='Seja bem Vindo ao programa',font='Verdana 14').pack()# não tinha importado o label do tkinter ele importo sozinho caso de erro importa o label
    janela.after(3000, janela.destroy)
    janela.mainloop()
tela_inicial()
"""


"""
def msg_perso(msg,titulo,segs):
    janela = Tk()
    janela.title(titulo)
    larg = 600
    alt = 80
    janela.geometry(f'{larg}x{alt}')
    Label(janela, text=msg,font='verdano 14').pack()
    janela.after(segs*1000,janela.destroy)#caso não coloque a função destroy a janela não se fexa sozinha e tem que multiplicar por 1000
    MessageBeep()#com a importação da biblioteca windound import messagebeep voce adiciona um som ao programa quando compilado
    janela.mainloop()

msg_perso('Ola seja bem vindo guilherme', 'Boas vindas a janela',3)
"""

"""
from tkinter.filedialog import askdirectory
from winsound import MessageBeep
from tkinter import Label, Tk
from os import system
system('cls')

def escolher():
    janela = Tk()
    janela.withdraw()# ele oculta a janela base
    diretorio = askdirectory()
    return diretorio

diretorio = escolher()
print(diretorio)
"""

"""
from tkinter.filedialog import askdirectory
from winsound import MessageBeep
from tkinter import Label, Tk
from os import system
system('cls')


def corrigidor(texto):
    corrigido = ' '.join(texto.split())# a sintaxe é .join(x(condição))
    return corrigido
texto = corrigidor('Guilherme dias     co    elho')
print(texto)
"""

def soma(lista_De_numeros):
    return sum(lista_De_numeros)
soma = soma ([5,5,5,5,5])
print(soma)




