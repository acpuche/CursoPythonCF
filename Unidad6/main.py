
# Al usar 'or' Python asignará el primer valor verdadero a la variable
# Lo anterior se hará de izquierda a derecha
variable = 'Cody' or 'CodigoFacilito'

variable = '' or 'CodigoFacilito'

variable = '' or 0 or [] or True

# Ejemplo de lo anterior:
listado = []
nombre = 'Cody'

if listado:
    variable = listado
else:
    variable = nombre

# Lo anterior se puede expresar en una línea de código

variable = listado or nombre

print(variable)