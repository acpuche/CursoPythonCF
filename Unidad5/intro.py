# Definicion
diccionario = {}
diccionario = dict()

# { llave : el valor el cual queremos asociar. }

diccionario = { "total": 55 }

diccionario = { "total": 55, "descuento": True, "subtotal": 15 }

diccionario = { "total": 55, 10: "Curso de Python", (1,2,3): True}

# Llaves 

# Un string ("total")
# Un numero entero (10)
# Una tupla que almacena números enteros (1,2,3)

# El equivalente a un json en python es un diccionario

diccionario = { 'Aura': 1, 'Daniela': 2, 'Marco': 3, 'Katy': 4}

diccionario.keys()

diccionario.values()

for key, value in diccionario.items():
    print(key, value)


# Método get permite definir un valor en caso de que no exista una llave

usuario = {
    'name': 'Aura Cristina',
    'age': 26,
    'job': 'C+odigoFacilito'
}

calificaciones = usuario.get('calificaciones', []) # Como no existe calificaciones se manda una lista vacia para evitar el error
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)


# Se puede usar comprehension
usuarios = ['Aura', 'Daniela', 'Marco', 'Katy']
diccionario = { usuario:position + 1 
for position, usuario in enumerate(usuarios)}
print(diccionario)


