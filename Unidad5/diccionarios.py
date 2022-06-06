elementos = {}

# Añadir nuevos elementos al diccionario
elementos['nombre'] = 'Cody' # crea la llave
elementos[(1,2,3)] = 'La llave es una tupla'

# modificar el valor para la llave nombre
elementos['nombre'] = 'CódigoFacilito' # actualiza el valor de la llave

print(elementos)
print(len(elementos)) # conocer la longitud del diccionario

# Si se repite la llave ésta tomará el último valor asignado a la llave
elementos2 = {'a':1, 'b':2, 'c':3, 'a':4}
print(elementos2)

