"""
Diccionarios {}

estructura datos de pares clave:valor
se accede a los elementos a traves de la clave, no importa la posición
las claves no se generan automaticamente, no hay un orden
las claves pueden ser String, numerico, incluso Boolean
los valores pueden ser: String, numerico, boolean, listas, diccionario u otro tipo de datos
Si la clave existe, modifico su valor, si no existe, se agrega el par clave:valor (se crea)

"""
from os import system
diccionario = {
    1: "uno",
    "dos": 2,
    3: ["a","b","c"], # lista dentro de diccionario
    "dicc": {"A":"A Mayuscula"},
    }

#Diccionario vacio
notas = {}
print(len(notas))#cero

notas = {
    "Camila": 7,
    "Antonio": 5,
    "Felipe": 6,
    "Daniela": 5,
    "Vicente": 7,
    "FELIPE": 2,
    "Vicente": 1,
}
system("clear")
print(len(notas))#
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7}

#Acceso a los elementos(valores)
print(notas["Camila"]) #7
print(notas["Antonio"])#5
print(notas["Felipe"]) #6
print(notas["Daniela"])#5
print(notas["Vicente"])#1 reemplaza a 7
#print(notas["felipe"])#KeyError: 'felipe'

print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7}
notas["Julio"] = 4
print(notas)#

#julio = {"nota1":7,"nota2":4}

#modificar par clave:valor
notas["Julio"] = 5
print(notas)#

#1RA FORMA: eliminar par clave:valor
del notas["FELIPE"]#del desaparece Todo 
print(notas)#

#2DA FORMA pop()-> al eliminar capturamos el valor 
eliminado = notas.pop("Camila")#notas["Camila"]
print("valor eliminado: ",eliminado)#
print(notas)#{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 5}

notas2 = {
    "Mijail":2,
    "Israel":1,
    "Felipe":7,
}

#notas.update(notas2)
#print(notas)#{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 5, 'Mijail': 2, 'Israel': 1}
notas2.update(notas)
print(notas2)#{'Mijail': 2, 'Israel': 1, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 5}
#COLISIONES: al existir duplicidad de claves, se conserva el valor del diccionario anexado

print(notas2.keys())
#dict_keys(['Mijail', 'Israel', 'Felipe', 'Antonio', 'Daniela', 'Vicente', 'Julio'])
print(notas2.values())
#dict_values([2, 1, 6, 5, 5, 1, 5])

print(type(None))#<class 'NoneType'>

print(notas2.items())#items como tal entrega lista de par clave:valor
#dict_items([('Mijail', 2), ('Israel', 1), ('Felipe', 6), ('Antonio', 5), ('Daniela', 5), ('Vicente', 1), ('Julio', 5)])

#get(clave)-> retorna el valor asociado a la clave
print(notas2.get('Antonio'))#5 (ya que antonio tenia valor 5)
print(notas2.get('Sofia'))#None (no existe la clave, entonces retorna x default 'None')
#se puede especificar el valor de retorno al no existir la clave
print(notas2.get('Sofia', "Valor no existe"))#Valor no existe
