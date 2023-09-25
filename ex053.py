
frase = str(input('Digite uma frase: ')).strip().upper()#logo no inicio ja começa a tratar a string removendo os espaços antes e colocando em maiculas
palavras = frase.split()#aqui o split vai separar a frase com base nos espaços em strings individuais
junto =  ''.join(palavras)#aqui no join ele vai juntas todas as strings e substituir pelo oque esta entre aspas ''
inverso = ''

for letra in range(len(junto)-1,-1,-1):#
    inverso += junto[letra]
print(f'O inverso de {junto}  é  {inverso}')
if junto == inverso:
    print('Temos um palindromo')
else:
    print('Não temos um palindromo')




