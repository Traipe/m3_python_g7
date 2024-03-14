"""" 
La velocidad de escape de un planeta se define como la mínima velocidad necesaria para
salir de un planeta venciendo la gravedad.
La velocidad de escape se calcula mediante la siguiente fórmula:
𝑉𝑒 = √2𝑔𝑟
Ve : corresponde a la Velocidad de Escape en [m/s].
g (gravedad): corresponde a la constante gravitacional en [m/s2].
r (radio ): Corresponde al radio del planeta en [m].

Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().
"""
#import math solo el necesario a utilizar, en este caso raíz cuadrada
from math import sqrt

#ASÍ SE HIZO EN CLASES
#paso 1
#capturar y almacenar datos ingresados por el usuario (por default input() lo almacena como string)
radio = input("ingrese el radio en km")
#6371 -> "6371"
#paso 2
#transformar string a numero
radio = float (radio) #-> la funcion float(), transforma un string a float
radio = float("6371") #-> radio = 6371 -> como num
#paso 3 
#transformar kilometros a metros (multiplicar por mil)
radio = radio * 1000 #radio = 6371 * 1000 -> radio = 6371000

#paso 1 para g 
constante_gravitacional = float(input("ingrese la constante gravitacional:"))
#9.8 -> "9.8"
#paso 2 para g 
#transformar string a numero float(constante_gravitacional)
#constante_gravitacional = float("9.8") -> constante_gravitacional = 9.8

#calculo formula 𝑉𝑒 = √2𝑔𝑟
multiplicacion = 2 * constante_gravitacional * radio

velocidad_escape = sqrt(multiplicacion)

print(f"La velocidad de Escape es {round(velocidad_escape,1)} [m/s]")



"""
Esto es lo qe hice yo
#import math solo el necesario a utilizar, en este caso raíz cuadrada
from math import sqrt

#datos de entrada 
print("ingrese el radio en kilometros:")

#radio
radio = float(input(""))
print("ingrese la constante g:")

#gravedad
gravedad = float(input(""))

#convertir el radio que estaba a km a metros, multiplicando radio por 1000
radio = radio * 1000

#calcular la velocidad de escape, multiplicando raiz x los elementos
ve = sqrt(2 * r * g)

#Mostrar la velocidad de escape con texto 
print(f"La velocidad de Escape es {ve} [m/s]")
"""