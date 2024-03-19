""" 
CONDICIONAL IF

Sis e cumple la condicion, entonces se ejecuta el codigo

if condicion: 
    #Codigo a ejecutar si es verdadero

elif:
    #codigo a ejecutar si la priemra no se cumple
    
else:    
    #codigo por default si no se ejecutan otros codigos
    
"""

edad = int(input("ingrese su edad: \n"))
if edad >=18: 
    print("eres mayor de edad")
elif edad ==18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")

print("\n")
if edad == 0:
    print("La edad es cero")    
elif edad%2 == 0:
    print("La edad es un numero par")
else:
    print("La edad es un numero impar")

print("\n")
print("Fin del programa")

