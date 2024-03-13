#division de enteros, resulta un float
print(100/20)
print(10 + 3.5)
print(10 - 3.5)
print(10 * 3.5)

#STRING -> cadena de caracteres
nombre='jimena'
edad = "44"
print('a123456!!!#$#%$&%')
print(edad)#imprimir el contenido de la variable
print("tu edad es "+edad)
numero=100

#duplicacion, solo es para los string
print(3*edad)#edad edad edad
print(3*numero)

print(type(edad))#<class 'str'>
print(3*edad)#444444

print(type(numero))
print(3*numero)#300

#metodo count()
print("kakaroto".count("roto"))

#metodo upper() y lower()
print("kAkArOtO".upper())#KAKAROTO
print("KaKaRoTo".lower())#kakaroto
print("KaKaRoTo".title())

#metodo count() y len()
print("17.785.838-2".count("."))#2
print(len("17.785.838-2"))#12
#print(len(123456778)) #un num no es un objeto

#join --> unir elementos separados
print(", ".join(["a","b","c"]))

print(" esto es\n un mensaje")
print(" Jelou Jelou\n mai frend")

#Tipo de Datos
entero = 9
decimal = 6.3
cadena = " esto es una cadena "
booleanos = True #True o False

print(type(entero)) #<class 'int'>
print(type(decimal)) #<class 'float'>
print(type(cadena)) #<class 'str'>
print(type(booleanos)) #<class 'bool'>

numero2 = 200
numero2 = numero2 + 100 #numero2 = 200 + 100

texto = "asd"
texto = texto + "qwe" #texto "asdqwe"

#precision de datos
promedio = (4+5+7)/3
print(f"el promedio es {promedio}")
print(f"resulta de la division {promedio:.4f}")
print(f"resulta de la division {1/9:.4f}")
print(f"resulta de la division {round(1/9,3)}")
print(f"resulta de la division {round(promedio,3)}")

#Ingreso de datos (INPUT)
nombre = input("Ingrese su nombre:\n")
print(nombre)
print(f"Tu nombre es {nombre}")
edad = input("Ingrese su edad:\n")
print(f"Tu edad es {edad}")
print(type(edad))#<class 'str'>

input("ingresa tu apellido")



