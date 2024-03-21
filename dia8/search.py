import sys, random

numero_buscar = int(sys.argv[1]) #número a buscar

lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista)#desordenar la lista, permanentemente
print(lista)

for posicion, numero in enumerate(lista):
    
    if numero_buscar == numero:
        print("Numero encontrado")
        break
    
print("Fuera del for")
print(f"el numero {numero_buscar} se encontro en la {posicion}") 