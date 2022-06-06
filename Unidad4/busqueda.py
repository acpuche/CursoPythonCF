titulo_curso = 'Curso profesional de Python, para aprender Python'

# Retornar la cantidad de coincidencias que se encuentren en el string
contador = titulo_curso.count('Python')

# Se pueden buscar caracteres
contador = titulo_curso.count('o')

print(contador)


# Se puede hacer por medio de otro método
print('Python' in titulo_curso)

# Para facilitar las búsquedar se recomienda estándarizar en minusculas o mayusculas
print('python' in titulo_curso.lower())

print('codigofacilito' not in titulo_curso)


# Identificar si el texto inicia con una palabra definida
print(titulo_curso.startswith('Curso'))

print(titulo_curso.endsswith('Python'))
