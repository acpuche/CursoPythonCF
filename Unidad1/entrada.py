nombre_completo = input('Ingresa tu nombre completo: ')

edad = input('Ingresa tu edad: ')
edad = int(edad) # conversión a entero

altura = input('Ingresa tu altura')
altura = float(altura)

autorizacion = input('¿Autorizas al programa? (si/no)')
autorizacion = autorizacion == 'si'

# Lo anterior se puede expresar en menor número de líneas de código de la siguiente manera
edad = int(input('Ingresa tu edad: '))
altura = float(input('Ingresa tu altura'))
autorizaion = input('¿Autorizas al programa? (si/no)') =='si'

print(edad)
print(type(edad))