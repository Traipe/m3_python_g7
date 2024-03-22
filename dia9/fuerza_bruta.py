""" 
Felipe Arias
Najla Gatica 
Lolett Llanquinao
Jimena Traipe

Consideraciones
● Utilizar from string import ascii_lowercase
○ ascii_lowercase es un string con todas las letras del abecedario en
minúsculas (sin la ñ).
● No considerar la ñ.
● Considera mayúsculas y minúsculas como una misma letra.
● Se considera "intento" cada vez que se compara una letra.

"""
#Actividad 3 - Fuerza bruta 

import getpass
from string import ascii_lowercase

password = getpass.getpass("Ingresa la contraseña:").lower()
#password = input("Ingresa la contraseña:").lower()

minusculas = ascii_lowercase
print(minusculas)
contador = 0

for caracter in password:
    print(caracter)
    for letra in minusculas:
        contador+=1
        if caracter == letra: 
            break

print(f"La contraseña fue forzada en {contador} intentos")

"""" 
respuesta terminal:
abcdefghijklmnopqrstuvwxyz
g
a
t
o
La contraseña fue forzada en 43 intentos

////
Ingresa la contraseña:
abcdefghijklmnopqrstuvwxyz
s
s
i
e
t
e
s
i
e
t
o
c
h
o
La contraseña fue forzada en 171 intentos

///
Ingresa la contraseña:
abcdefghijklmnopqrstuvwxyz
m
a
w
i
z
a
n
t
u
La contraseña fue forzada en 128 intentos

"""