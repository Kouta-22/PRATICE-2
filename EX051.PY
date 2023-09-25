

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

t1 = eval(input('Digite os primeiro TERMO: '))
r1 = eval(input('Digite a RAZÂO: '))
dez = t1 + (11-1) * r1# essa é a formula não entendi
for c in range (t1, dez,r1):#nota ele armazenou no C
    print(c,end=' ↠ ')
print('ACABOU')


