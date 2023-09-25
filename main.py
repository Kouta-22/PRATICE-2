
#comentarios
"""""
peso = eval(input("digite peso "))
altura = eval(input("digite altura "))
imc = peso/(altura**2)
print("o valor do imc é: ",imc)

como usa comando print
idade = 20
print("a idade é = ", idade+1)

outra forma de formatação
idade = 20
print(f'a idade é = {idade + 1}')

impressão de sequencia 
str = 'hello word'
print(str[0:4])  

Também é possível imprimir a string como lida da direita para a esquerda. Para isso, deve-se utilizar [::-1]
str='helou word'
print(str[::-1])


exercicio
def fc(x,y):
    s=0
    a = x.lower()
    for i in a:
        if(i==y):
            s = s + 1
            return s

a = 'Aracaju/Sergipe'
x = fc(a,'a')*100
y = fc(a,'e')*10
z = fc(a,'i')
print(x+z+y)
"""

















