"""  
SETS
conjunto de datos que no permite duplicados
no es ordenado, se escriben con {}
"""


muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

# no hay duplicados, sólo valores únicos
print(muchos_animales)
#{'Hurón', 'Erizo de Tierra', 'Tortuga', 'Perro', 'Hamster', 'Gato'}

muchos_animales.add("Gallina")#agrega un elemento al set
print(muchos_animales)
#{'Gallina', 'Gato', 'Hurón', 'Perro', 'Erizo de Tierra', 'Hamster', 'Tortuga'}
#print(muchos_animales('Gallina'))#TypeError: 'set' object is not callable
#print(muchos_animales['Gallina'])#TypeError: 'set' object is not callable
muchos_animales.remove("Hurón")
print(muchos_animales)#{'Perro', 'Hamster', 'Tortuga', 'Erizo de Tierra', 'Gato', 'Gallina'}    

#Podré quitar algo que no existe?
#muchos_animales.remove("Leon")#KeyError: 'Leon'
print(muchos_animales)
muchos_animales.discard("Leon")#Si existe, lo quito, sino, no hago nada
print(muchos_animales)
muchos_animales.pop()#{'Erizo de Tierra', 'Gato', 'Gallina', 'Tortuga', 'Perro'}
print(muchos_animales)#aqui elimino 'Hamster'
muchos_animales.clear()
print(muchos_animales)#set() quita todos los elementos dentro del set

print(muchos_animales.__dir__())
""" 
['__new__', '__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__iter__', '__init__', '__sub__', '__rsub__', '__and__', '__rand__', '__xor__', '__rxor__', '__or__', '__ror__', '__isub__', '__iand__', '__ixor__', '__ior__', '__len__', '__contains__', 'add', 'clear', 'copy', 'discard', 'difference', 'difference_update', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', '__reduce__', 'remove', '__sizeof__', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update', '__class_getitem__', '__doc__', '__str__', '__setattr__', '__delattr__', '__reduce_ex__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__dir__', '__class__']
"""
print("")
print(dir(muchos_animales))
""" 
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

