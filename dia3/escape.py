#import math solo el necesario a utilizar, en este caso raíz cuadrada
from math import sqrt

#datos de entrada 
print("ingrese el radio en kilometros:")
#radio
r = float(input(""))
print("ingrese la constante g:")
#gravedad
g = float(input(""))

#convertir el radio que estaba a km a metros, multiplicando radio por 1000
r = r * 1000

#calcular la velocidad de escape, multiplicando raiz x los elementos
ve = sqrt(2 * r * g)

#Mostrar la velocidad de escape con texto 
print(f"La velocidad de Escape es {ve} [m/s]")
