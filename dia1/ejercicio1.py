#esto es un comentario de una linea
""" 
comentario 
de mas 
de una 
linea
"""
print("Trabajando para su futuro en vscode")
print(2+2)
print(8-3)
print(4*3)
#print(2/0) aqui se detiene por el error
print(144/7) #en la division aunque trabaje num enteros siempre sera un float

numero = 23
print(numero)

#Limitantes
#No esta permitido sumar letras y numeros
# print("texto"+12) #TypeError: can only concatenate str (not "int") to str
print("texto",12) 
#concatenar = "texto"+12
print("texto"+"34") 


#INTERPOLACION
print (f"eln numero es {numero+2}")
nombre = "Victor"
print(f"Tu nombre es{nombre} \n y tu edad es {numero}")
print("Tu nombre es "+nombre)
#string.format
print("Tu nombre es {} y tu edad es {}".format(nombre,numero))
# formato con %: %s para string y %d para numeros
print("Tu nombre es %s y tu edad es %d")
# metodo con cadena
apellido = "traiPe urRejola"
print(apellido.title())