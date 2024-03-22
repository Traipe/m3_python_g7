""" 
Felipe Arias
Najla Gatica 
Lolett Llanquinao
Jimena Traipe
"""


#ejercicio Filtrado Compacto

import sys

# Diccionario de ventas
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000
}

# Usuario ingresa el umbral en consola
umbral_ventas = int(sys.argv[1])

# Filtra los meses mayores al umbral y crea el nuevo diccionario (meses_mayor_a_umbral_ventas)
#Comprehension
meses_mayor_a_umbral_ventas = {mes: ventas_mes for mes, ventas_mes in ventas.items() if ventas_mes > umbral_ventas}

# Imprime el resultado del nuevo diccionario (meses_mayor_a_umbral_ventas)
print(meses_mayor_a_umbral_ventas)

#ingresar en la consola 
# python dia9/mayor_a.py 40000