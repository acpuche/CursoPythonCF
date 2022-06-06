"""
Contexto: asignar un color según la calificación
Al no saber el color a asignar se declara como None
"""

calificacion = 10
color = None

if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'

# Lo anterior se puede representar con menor número de líneas de código

color = 'Verde' if calificacion >= 7 else 'Rojo' # else es obligatorio al usar esta representación de una línea
print(calificacion,color)