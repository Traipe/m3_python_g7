""" 
Grupo 3 
Yanina Belmar
Yessenia Millar
Jimena Traipe

A continuación, se muestra cómo crear un programa que filtre todos los números
de una lista que sean menores a 1000. Esto es lo mismo que decir "seleccionar
todos los elementos mayor o iguales a mil".
Transformarlo en un List Comprehension

"""
a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n): #lo que estamos utilizando
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)
print("")
#resultado: [1000, 5000, 10000, 5000]
##[expresión1 if condición1 else expresión2 for variable in iterable]
#siguiendo la logica 
filtrado_numeros = [a[i]  for i in range(n) if a[i] >= 1000] #se utiliza la tercera expresion de comprehesion
#si el if esta antes del for, DEBE haber un else
#si solo hau 1 if, va despues de for in range(n)
print(filtrado_numeros)


##Colaborativo
