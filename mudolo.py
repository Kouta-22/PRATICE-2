from tkinter.filedialog import askdirectory
from winsound import MessageBeep
from tkinter import Label, Tk
from os import system
system('cls')

def msg_pers(msg,titulo,segundos):
    janela = Tk()
    janela.title(titulo)
    Label(janela,text=msg).pack()
    janela.after(segundos *1000, janela.destroy)#o after trata em milissegundo 
    janela.mainloop()
#chamamento de função
msg_pers('Bom dia, Guilherme!','Boas vindas',3)
#
#
#
def escolha_diretorio():
    janela = Tk
    janela.withdraw()
    diretorio = askdirectory
    return diretorio
diretorio = escolha_diretorio
#
#
#
def fun1(texto):
    corrigir = ' '.join(texto.split())
    return corrigir

texto = fun1 ('  guilherme dias    coelho     ')
print(texto)
#
#
#
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
#
#
#
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
#
#
#
def escolher():
    janela = Tk()
    janela.withdraw()# ele oculta a janela base
    diretorio = askdirectory()
    return diretorio

diretorio = escolher()
print(diretorio)
#
#
#
def corrigidor(texto):
    corrigido = ' '.join(texto.split())# a sintaxe é .join(x(condição))
    return corrigido
texto = corrigidor('Guilherme dias     co    elho')
print(texto)
#
#
#
