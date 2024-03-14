#import math
from math import sqrt

#datos de entrada
print("ingrese el radio en kilometros:")
r = float(input(""))
print("ingrese la constante g:")
g = float(input(""))

#convertir el radio a metros
r = r * 1000

#calcular la velocidad de escape
ve = sqrt(2 * r * g)

#Mostrar la velocidad de escape
print(f"La velocidad de Escape es {ve} [m/s]")
