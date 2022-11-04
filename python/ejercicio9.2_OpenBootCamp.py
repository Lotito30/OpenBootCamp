from functools import reduce

lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

filtrar = filter(lambda x: x % 2 == 1,lista_numeros)
reducir = reduce(lambda a,b: a+b,filtrar)

print(reducir)