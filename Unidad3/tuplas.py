cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')

primer_curso = cursos[0]
print(primer_curso)

ultimo_curso = cursos[-1]
print(ultimo_curso)

# Generar subtuplas

sub_tupla = cursos[0:3] # el índice final no es tomado en cuenta 
sub_tupla = cursos[:3]
print(sub_tupla)