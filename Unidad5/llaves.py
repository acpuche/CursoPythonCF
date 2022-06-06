from this import d


diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

"""
Llaves, items, valores
Se  mantiene el orden usado al crear el diccionario
Se convierten a tuplas para que posteriormente no puedan ser modificados
"""

# Conocer las llaves del diccionario y se convierte a tuplas
llaves = tuple(diccionario.keys())
print(llaves)

# Se obtienen los valores y se convierte a tuplas
valores = tuple(diccionario.keys())
print(valores)

# Se obtienen los items y se convierte a tuplas
elementos = tuple(diccionario.items)
print(elementos)