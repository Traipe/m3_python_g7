""" 
Dada la información de ventas de 3 meses:

Mes (Clave)      Ventas (Valor)
Octubre          65000
Noviembre        68000
Diciembre        72000

1. Convertir la tabla en un diccionario
2. Modificar el diccionario para incrementar las ventas en un 10%.
3. Hacer un nuevo diccionario pero con las ventas disminuidas un 20%.

"""


# Crear el diccionario con la información de ventas
ventas = {
    "Octubre": 65000,
    "Noviembre": 68000,
    "Diciembre": 72000
}

# Mostrar el diccionario original
print("Diccionario original:")
print(ventas)

# Incrementar las ventas en un 10%
ventas_incrementadas = {mes: ventas * 1.10 for mes, ventas in ventas.items()}

# Mostrar el diccionario con ventas incrementadas
print("\nDiccionario con ventas incrementadas en un 10%:")
print(ventas_incrementadas)

# Disminuir las ventas en un 20%
ventas_disminuidas = {mes: ventas * 0.80 for mes, ventas in ventas.items()}

# Mostrar el diccionario con ventas disminuidas
print("\nDiccionario con ventas disminuidas en un 20%:")
print(ventas_disminuidas)


""""   
Referencia

##DICCIONARIO Comprehesion, se guarda con llave ({})
claves = ['nombre','apellido','edad','altura']
valores = ['Jimena','Traipe', 33, 1.59]
diccionario2 = {k:v for k,v in zip(claves, valores)}#almacenando dentro de una variable el comprehesion. 
print(diccionario2)
"""