r1 = eval(input('Digite um valor: '))#cada um desses seguimento tem que ser menor que a soma do comprimento dos outros 2 
r2 = eval(input('Digite um valor: '))#cada um desses seguimento tem que ser menor que a soma do comprimento dos outros 2 
r3 = eval(input('Digite um valor: '))#cada um desses seguimento tem que ser menor que a soma do comprimento dos outros 2 



if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    
    if r1 == r2 and r2 == r3: 
        print('Esses seguimentos formam um triangulo EQUILATERO !!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Esses seguimentor formam um triangulo ESCALENO !!')
    else:
        print('Esses seguimentos formam um triangulo ISOCELES !!')
else:
    print('Com esses seguimentos não é possivel forma um triangulo')


