import sys, time
#argumento es el dato que ingresa el usuario sin una solicitud de por medio
print(sys.argv)#['dia7/bomba.py', '8']
print(sys.argv[0])#el primer elemento queda en esta posicion (el archivo)
print(sys.argv[1])

i = int(sys.argv[1])#el 1 es la posicion de esa lista

while i >0:
    print(f"el valor de i {i}")
    time.sleep(1)#tiempo de espera 1 segundo
    i -= 1 #decrementando (restando 1)
    
print("BUUUUUUUM!!!!!!")