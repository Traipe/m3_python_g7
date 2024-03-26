""" EJEMPLO EN CLASES CON MASCOTA"""
from os import system

mascotas = {} 

cant_mascotas = int(input("ingrese cantidad de mascotas a ingresar"))#3

for i in range(cant_mascotas): #0,1,2

    mascota = {
    "nombre":"",
    "raza":"",
    "peso":0.0,
    "chip": True,
       
    }

    #Recorrer un diccionario x default
    """
    for clave in mascota:
    print(clave)
    mascota[clave] = input(f" ingrese la {clave} de su mascota")#el input captura los datos como string
    """ 

    for key in mascota.keys():
    #print(key)
        mascota[key] = input(f" ingrese la {key} de su mascota")
    
    print(mascota)

    print("")
    # Accedemos a los valores en nuestro diccionario
    for valor in mascota.values(): #imprime cada uno de los valores ingresados
        print(valor)

    print("")
    for clave,valor in mascota.items(): #imprime cada uno de los valores ingresados
        print(f"clave {clave} - valor {valor}")
    
    mascotas[mascota["nombre"]] = mascota
    #mascotas["Pire"] = mascota
    
print(mascotas)#
{
{'Pire': {'nombre': 'Pire', 'raza': 'Bosque de Noruega', 'peso': '3kg', 'chip': 'false'}, 
 'Gorde': {'nombre': 'Gorde', 'raza': 'Bombay', 'peso': '2.5kg', 'chip': 'false'}, 
 'Niño': {'nombre': 'Niño', 'raza': 'bombay', 'peso': '3.5kg', 'chip': 'false'}}
}
""" 
{
... {'Pire': {'nombre': 'Pire', 'raza': 'Bosque de Noruega', 'peso': '3kg', 'chip': 'false'},
...  'Gorde': {'nombre': 'Gorde', 'raza': 'Bombay', 'peso': '2.5kg', 'chip': 'false'},
...  'Niño': {'nombre': 'Niño', 'raza': 'bombay', 'peso': '3.5kg', 'chip': 'false'}}
... }
"""

#acceder a un diccionario dentro de un diccionario(APUNTE PROFE)
#mascotas["ayun"]            => {'nombre': 'ayun', 'raza': 'bull', 'peso': '12', 'chip': 'si'}
#mascotas["ayun"]["nombre"]  => "ayun"

#mascotas["ayun"].pop("nombre")




    
