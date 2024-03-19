#crear un script donde el usuario de ingreso de password 
#donde el largo minimo es de 6 caracteres
import getpass
#password=input("ingrese su contraseña: ")
password = getpass.getpass("ingrese su contraseña:")

if password == "12345":
    print("El password es incorrecto")

elif len(password)<6:
    print("El password es demasiado corto")

