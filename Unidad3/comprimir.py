lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

lista2 = [100, 200, 300, 400, 500]

resultado = zip(lista, tupla, lista2) # -> zip
resultado = tuple(resultado) # -> tupla con subtuplas
# de los elementos de la lista y la tupla combinados
# ((10, 1), (20, 2), (30, 3), (40, 4), (50, 5))
print(resultado)

# Si la lista no contiene la misma cantidad de elementos, al realizar la 
# combinación serán omitidos los sobrantes
lista3 = [1000, 2000, 3000, 4000, 5000, 6000]
resultado2 = zip(lista, tupla, lista2, lista3) # -> zip
resultado2 = tuple(resultado2) # -> tupla con subtuplas
print(resultado2)
