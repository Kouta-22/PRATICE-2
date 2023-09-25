r1 = eval(input('Digite um valor: '))#cada um desses seguimento tem que ser menor que a soma do comprimento dos outros 2 
r2 = eval(input('Digite um valor: '))#cada um desses seguimento tem que ser menor que a soma do comprimento dos outros 2 
r3 = eval(input('Digite um valor: '))#cada um desses seguimento tem que ser menor que a soma do comprimento dos outros 2 

tot1 = r1 < r2 + r3
tot2 = r2 < r1 + r3
tot3 = r3 < r1 + r2

if tot1 < tot2:
    print('Não da para forma um triangulo')
if tot2 < tot1:
    print('Não da para forma um triangulo')
if tot3 < tot1:
    print('Não da para forma um triangulo')
else:
    print('Forma um triangulo')


    





