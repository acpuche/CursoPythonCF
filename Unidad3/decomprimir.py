numeros = (1,2,3,4)

# se asigna cada uno de los valores de la tupla a una variable
uno, dos, tres, cuatro = numeros 


# Si no conocemos el número de elementos de la tupla 
numeros2 = (1,2,3,4,5,6,7,8,9,10)
uno, dos, tres, cuatro, *resto_valores = numeros2 # el * denota lista

uno, dos, tres, cuatro, *_ = numeros2 # notación *_ para descartar el resto de los valores

# Si se quieren omitir los elementos después del 4 conservando los últimos dos
uno, dos, tres, cuatro, *_, nueve, diez = numeros2 

# Si se quieren obtener todos los números excepto el 2 y del 4:8
uno, _, tres, cuatro, *_, nueve, diez = numeros2  

"""
* -> lista
_ -> Omitir valor
"""

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)