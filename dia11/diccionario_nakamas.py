# Paso 1: Creamos un diccionario nakamas de One Piece con tripulantes de la serie
tripulacion = {
    'capitan': 'Monkey D. Luffy',  # Capitan
    'nakama1': 'Zoro',             # 1er nakama
    'nakama2': 'Nami',             # Seg nakama
    'nakama3': 'Usopp',            # 3er nakama
    'nakama4': 'Sanji'             # 4to nakama
}

# paso 2: Imprime la tripulacion actual(primera tripulacion) 
print("Tripulacion actual:")
for puesto, nombre in tripulacion.items(): #bucle for para recorrer dicc
    print(f"{puesto}: {nombre}") #imprime la clave y el valor para la iteracion
#OSEA imprime cada clave y su valor correspondiente en dicc tripulacion


# Paso 3: El capitan añade un nuevo nakama
nuevo_nakama = 'Chopper' #variable nueva 'nuevo_nakama' & valor nuevo nakama
tripulacion['nakama5'] = nuevo_nakama #nueva clave de entrada al dicc 'nakama5'
#OSEA Se crea un nuevo miembro de la tripulacion


# Imprime la tripulacion actualizada con el nuevo integrante
print("\n Un nuevo nakama:")
#imprime cada clave y su respectivo valor en la tripulacion actual
for puesto, nombre in tripulacion.items(): #aki ocupe items porke accedo a clave&valor para iterar en un bucle for
    print(f"{puesto}: {nombre}")
#OSEA muestra la tripulacion actual desps de agregar el nuevo nakama