""" 
TUPLAS
Conjunto de datos ordenados e inmutables
Se escriben con paréntesis () SIEMPRE
"""

tupla1 =(1,3,5,7,9)
print(tupla1)# (1, 3, 5, 7, 9)
print(type(tupla1))#<class 'tuple'>
tupla2 = ("nombre", "Jimena")

nom, texto = tupla2
print(nom)
print(texto)
print(tupla2[0])#nombre
print(tupla2[1])#Jimena
#print(tupla2[2])#IndexError: tuple index out of range
#tupla2[2] ="jelou"#TypeError: 'tuple' object does not support item assignment
#ocurre el error porque las tuplas son INMUTABLES

#INMUTABLES
#tupla2[2] = "jelou"#TypeError: 'tuple' object does not support item assignment
#tupla2[1] = "jelou" #TypeError: 'tuple' object does not support item assignment
print("")
#Iterar tupla
for num in tupla1:
    print(num)
    
#CUIDADO
# TANTO EL DICCIONARIO O LA LISTA PERMITE ELIMINAR ELEMENTOS

list_dicc1 = list({"nota1":5,"nota2":6}.items())
print(list_dicc1)#[('nota1', 5), ('nota2', 6)]
print(list_dicc1[0])#('nota1', 5)
print(list_dicc1[1])#('nota2', 6)
print("")
# ('nota1', 5)
# ('nota2', 6)
print(list_dicc1[0][0])#'nota1'
print(list_dicc1[0][1])#5
print(list_dicc1[1][0])#'nota2'
print(list_dicc1[1][1])#6
#Fila Columna
#[0][0]
