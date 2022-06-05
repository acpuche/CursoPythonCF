lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

# Obtener el primer elemento dentro del listado
primer_curso = lista_cursos[0]
ultimo_curso = lista_cursos[-1]
#print(primer_curso)
#print(ultimo_curso)

# Reemplazar valor del elemento

lista_cursos[4] = 'Rust'
#print(lista_cursos)

# Creación de sublista, <lista> = [start:end]
sub_lista = lista_cursos[0:3]

# Obtener todos los elementos de la lista <lista> = [start:]
sub_lista = lista_cursos[1:]

# Obtener los elementos de una lista hasta el indice indicado <lista> = [:end]
sub_lista = lista_cursos[:4]

# Indicar saltos para generar la lista <lista> = [start:end:skip]
sub_lista = lista_cursos[1:5:2]

# Generar sublista con todos los elementos de la lista original
sub_lista = lista_cursos[:]

# Obtener los elementos de una lista con saltos de dos en dos
sub_lista = lista_cursos[::2]

# Obtener una sublista con los elementos a la inversa
sub_lista = lista_cursos[::-1]

#print(sub_lista)
"""
Modificar listas
"""
# Añadir elementos a las listas, se añaden al final
lista_cursos.append('MongoDB')
lista_cursos.append('C$#')
lista_cursos.append(10) # Se puede agregar cualquier tipo de dato, sin embargo
# procurar tener listas con el mismo tipo de elemmentos.

# Conocer la longitud de una lista 
#print (len(lista_cursos))

# Añadir nuevo elemento en posición determinada, los otros elementos desplazan los idx
lista_cursos.insert(1,'Rails')
lista_cursos.insert(0,'Pygame')

# Se crea otra lista
lista_cursos_2 = ['C','C++','Docker']

# Añadir los elementos de lista cursos 2 a los de lista cursos, se añade al final
lista_cursos.extend(lista_cursos_2)

# Eliminar elementos de la lista
lista_cursos.remove('MongoDB')

del lista_cursos[0] # Se elimina el elemento contenido en el idx 0
del lista_cursos[-1]# Se elimina el elemento contenido en el último idx

# Eliminar todos los elementos de la lista o resetear
lista_cursos.clear()

#print(lista_cursos)
#print(lista_cursos_2)


"""
Métodos de listas
""" 
lista = [8,90,1,5,44,132,600,3,4]

# Ordenar listas
lista.sort() # ordena por defecto la lista de menor a mayor
lista.sort(reverse=True) # Ordena de mayor a menor

# Conocer el número mayor y menor de la lista
lista.sort()
min_num = lista[0] # numero minimo en la lista, min(lista)
max_num = lista[-1] # numero mayor en la lista, max (lista)

# Identificar la presencia de un elemento en la lista
#print(5 in lista)

# Identificar la no presencia de un elemento en la lista
#print(11 not in lista)

#print(lista)

"""
Index
"""

# Una vez cerificada la presencia de un elemento en la lista se puede conocer su ubicación
print(5 in lista)

index = lista.index(5) # EL método index solo retorna la primera ubicación del elemento
print(index)