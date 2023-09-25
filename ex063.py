#sequencia de finabocci

num = eval(input('Digite um numero para para sequencia de finabocci: '))
num1 = 0
num2 = 1

for c in range(0,num):
    

    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(f' ->{num3}', end=' ')
    c +=1









