 
#while condicion: 
    #codigo a ejecutar


#import getpass
"""
password = getpass.getpass("Ingrese su contraseña:\n")

while len(password) < 6:
    password = input("Ingrese su contraseña con mínimo 6 caracteres: \n")

while password != "hola mundo":
 password = getpass.getpass("La clave secreta no es correcta. Intenta otra vez.")

print("\nContraseña correcta. Bienvenide a este programa")
#resto del programa
print("Fin del programa")
"""
#Iteracion de n veces
i = 0
while i < 10:
    print(f"El valor de i es: {i}")
    i+=1 #i = i + 1 #incremento en 1
    
print(f"fuera del while, valor de i= {i}")

"""
while True:
    print("acciones infinitas")
    if condicion:
    else:
        break #salir del bucle
"""

saludo = "hola"
saludo = saludo + " mundo"
print(saludo)
saludo += "chao"
print(saludo)
