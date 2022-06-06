nombre = 'Aura Cristina'
apellido = 'Puche'

# Método 1
nombre_completo = nombre + ' ' + apellido

# Método 2
# El primer %s tomará el valor de nombre y el segundo %s tomará el valor de apellido
nombre_completo = 'Miss %s %s %s' %(nombre, apellido, 'Sarmiento')

# Método format y placerholders
nombre_completo = 'Miss {} {} {}'.format(nombre,apellido, 'Sarmiento')

# Es posible nombrar los place holders y definir parámetros
# los cuales se pueden cambiar de posición y mantener su valor
nombre_completo = 'Miss {nombre} {primer_apellido} {segundo_apellido}'.format(
    nombre=nombre,
    primer_apellido=apellido,
    segundo_apellido='Sarmiento'
)

"""
Interpolación
"""

# FStrings, se pone la letra f al inicio
nombre_completo = f'Miss {nombre} {apellido} {"Sarmiento"} {10 * 20}' # el string se debe definir con comillas dobles

print(nombre_completo)