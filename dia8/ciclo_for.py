""" 
CICLO FOR 
for variable in iterable
"""
#[0,1,2,3,4,5,6,7,8,9] x default va a partir desde el cero
for i in range(10): #aqui 10 es el valor de término, x lo tanto no es considerado para range
    print(i)
print("")    
#[4,5,6,7,8,9]
for i in range(4,10):
    print(i)
print("")   
for i in range(4,10,2):
    print(i)
    
""" for javascript
for (let index = 4; index < 10; index++) {
    console.log(i);
}
"""
print("")  
#Lista
numeros=[2,"4",True,3,"5"]
for numero in numeros:
    print(numero)
    
print("")  
#String->similares a las listas
texto = "Hola Mundo"
for caracter in texto:
    print(caracter)
    
    
#Diccionario, se componen de elementos (clave:valor)
datos_personales={
    "Nombre": "Jimena",
    "Apellido": "Traipe",
    "edad": 32,
}

#imprimir las claves
for clave in datos_personales:
    print(clave)#imprime la clave

print("")  
#imprime los valores
for clave in datos_personales:
    print(datos_personales[clave])#

print("")  
#imprime clave, valor
for clave, valor in datos_personales.items():
    print(f"clave: {clave} - valor: {valor}")#
    
for par in datos_personales.items():
    print(par)#
    
print("")
for clave in datos_personales.keys():
    print(clave)#

print("")
for valor in datos_personales.values():
    print(valor)#
print("")    
##ENUMERATE
for posicion,caracter in enumerate(texto): 
    print(f"la posicion {posicion} del caracter {caracter}")
print("")  
for posicion,numero in enumerate(numeros): 
    print(f"la posicion {posicion} del numero {numero}")
    
print("")    
    
prefijo = ['La','El','La','El','los']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')
    
print("")

##BREAK
numeros=[2,"4",True,3,"5"],{"clave":"valor"}
for numero in numeros:
    print(numero)
    if numero == 3:
        break
    
print("fuera del for")

