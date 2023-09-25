"""
valor = 20
 
def multiplica(fator):
    global valor
    valor = valor * fator
    print(f"Resultado {valor}")
 
multiplica(3)
multiplica(3)

valor = 20
 
def multiplica(valor, fator):
    valor = valor * fator
    return valor
 
print("Resultado", multiplica(valor, 3))
print("Resultado", multiplica(valor, 3))

"""
"""
valores = [10, 20, 30]#começa do 0 1 2 

def altera_lista(lista):
    lista[2] = lista[2] + 10
    return lista
 
print("Nova lista", altera_lista(valores))# ele altera o valor da lista e acrescenta mais 10 da função 
print("Nova lista", altera_lista(valores))# ele faz novamente porem com o valor alterado somando mais 20"""
#
#
#
"""
valores = [10, 20, 30]
 
def altera_lista(lista):
    nova_lista = list(lista)# ele usa a função list
    nova_lista[2] = nova_lista[2] + 10
    return nova_lista#tem que chamar nova lista caso chame lista novamente ele retorna apenas os valores
 
print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))

"""
#
#
#
"""
def multiplicar_por(multiplicador):
    def multi(multiplicando):
           return multiplicando * multiplicador
           #    return lambda multiplicando: multiplicando * multiplicador
    return multi #outrar forma de fazer pe com lambida ^^^ crinado o parametro multiplicando e usando ele apos :: sendo multiplicando * multiplicador a função
 
multiplicar_por_10 = multiplicar_por(10)
print(multiplicar_por_10(1))
print(multiplicar_por_10(2))
 
multiplicar_por_5 = multiplicar_por(5)
print(multiplicar_por_5(1))
print(multiplicar_por_5(2))

"""
#
#
#
"""
lista = [1, 2, 3, 4, 5]
 
nova_lista = map(lambda item: item * 3, lista)
print(list(nova_lista))#nota tem que usar a função list para imprimir 
"""
#
#
#
"""
lista = [1, 2, 3, 4, 5]
 
def triplica_itens(iterable):
    lista_aux = []
    for item in iterable:
        lista_aux.append(item*3)
    return lista_aux
 
nova_lista = triplica_itens(lista)
print(nova_lista)"""




"""
metodo normal
lista = [1, 2, 3, 4, 5]
 
def impares(iterable):
    lista_aux = []
    for item in iterable:
        if item % 2 != 0:
            lista_aux.append(item)
    return lista_aux
 
nova_lista = impares(lista)
print(nova_lista)
"""
"""
METODO FILTER
lista = [1, 2, 3, 4, 5]

def impar(item):
    return item % 2 != 0
 
nova_lista = filter(impar, lista)
print(list(nova_lista))
"""

"""
lista = [1, 2, 3, 4, 5]
 
nova_lista = filter(lambda item: item % 2 != 0, lista)
print(list(nova_lista))

"""







