cursos = ['Python', 'Django', 'Flask']

niveles = ('Basico', 'Intermedio', 'Avanzado')

# Generar tupla a partir de una lista
cursos_tupla = tuple(cursos)
print(cursos_tupla)
print(type(cursos_tupla))

# Generar una lista a partir de una tupla
niveles_lista = list(niveles)
print(niveles_lista)
print(type(niveles_lista))