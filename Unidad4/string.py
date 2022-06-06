"""
Método Split
"""

lenguajes = 'Python Ruby Java Rust C++ C'

listado_lenguajes = lenguajes.split() # Cada espacio denota un nuevo elemento
print(listado_lenguajes)

# Si se quiere dividir un string que no está separado por espacios sino 
# por otro caracter
lenguajes2 = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes2 = lenguajes2.split('-') 
print(listado_lenguajes2)

# Si queremos dividir por un par de coincidencias y no todas como lo hizo
# anteriormente:

lenguajes3 = 'Python/*/Ruby/*/Java/*/Rust/*/C++/*/C'
listado_lenguajes3 = lenguajes3.split('/*/', 2) # divida dos veces 
print(listado_lenguajes3)


"""
Método Join
"""
lenguajes4 = ['Python', 'Ruby', 'Java', 'Rust']

# unirá todos los elementos de la lista mediante un caracter
string_lenguajes = ' '.join(lenguajes4) # unión por medio de un espacio
print (string_lenguajes)

