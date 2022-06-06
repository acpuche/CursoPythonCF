diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

"""
Método del
"""
# Eliminar elemento con llave a

del diccionario['a']

"""
Método pop
"""
valor = diccionario.pop('b')

print(diccionario)
print(valor)

# Si se intenta eliminar una llave que no existe con ambos métodos saldrá error
# Se debe verificar previamente si el elemento existe 

diccionario.clear() # Se eliminan todos los elementos del diccionario

