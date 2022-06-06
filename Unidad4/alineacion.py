mensaje = 'Hola mundo!'

# ljust -> Justificar a la Izquierda
# rjust -> Justificar a la derecha
# center -> Centrar
# Los anteriores no modifican el string originar sino que generan uno nuevo

#mensaje = mensaje.ljust(20) # Se añaden 20 espacios a la derecha del string

#mensaje = mensaje.rjust(20) # Se añaden 20 espacios a la izquierda del string

mensaje = mensaje.center(20) 

print(mensaje)