

cant_notas = int(input("Ingrese cantidad de notas"))
i = 1 
suma_notas = 0
while i <= cant_notas:
    nota = float(input(f"Ingresa tu {i} nota\n"))
    suma_notas = suma_notas + nota
    i +=1
    
print(f"El promedio de notas es: {round(suma_notas/cant_notas,2)}\n")