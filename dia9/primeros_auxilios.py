""" 
Felipe Arias
Najla Gatica 
Lolett Llanquinao
Jimena Traipe
"""
def primeros_auxilios():
    print("¡Bienvenido a la aplicación de primeros auxilios!")
    print("Por favor, responde las siguientes preguntas para obtener ayuda:")

    
respuesta = input("¿La persona necesita atención médica inmediata? (si/no): ").lower()
if respuesta == "si":
            print("Llevar a la persona al hospital de inmediato.")
            print("Fin.")
            
else:
            print("Abre la vía aérea.")

            respuesta = input("¿La persona está respirando? (si/no): ").lower()
            if respuesta == "si":
                print("Permite la ventilación.")
            else:
                print("Administra 5 ventilaciones y llama a la ambulancia.")
while True:
            respuesta = input("¿La persona tiene signos de vida? (si/no): ").lower()
            if respuesta == "si":
                print("Espera a la ambulancia.")
                respuesta = input("¿Ha llegado la ambulancia? (si/no): ").lower()
                if respuesta == "si":
                    print("Fin.")
                    break
            else:
                print("Realiza compresiones torácicas hasta que llegue la ambulancia.")

primeros_auxilios()