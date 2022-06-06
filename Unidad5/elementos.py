diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

# Obtener el valor de la llave d
valor = diccionario['d'] # siempre y cuando la llave exista sino sale error

# Evitar el error ante la ausencia de una llave
print('a' in diccionario) # Existe la llave a en el diccionario?

print(valor)

"""
Método get
"""

valor2 = diccionario.get('d')

# obtener el valor de una llave que no exista
valor2 = diccionario.get('z') # retorna None, no error

valor2 = diccionario.get('z', 'La llave no existe en el dic') # se añade mensaje en caso de que no exista

print(valor2)


"""
Método setdefault
Permite obtener el valor de una llave, en caso de que no exista se añade
al diccionario con su correspondiente valor
"""

valor3 = diccionario.setdefault('e', 5)
print(valor3)
print(diccionario)