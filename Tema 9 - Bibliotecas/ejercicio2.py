from functools import reduce

def reducir(lista): 
    #devuelve 1 cuando es impar
    resultado = list(filter((lambda x: x % 2), lista)) 
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)

lista = list(range(10))

reducir(lista)