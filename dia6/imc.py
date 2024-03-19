#Desafio IMC Actividad 1
#Indicar al usuario que ingrese los datos solicitados

peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en centimetros: "))

#pasar cm a mts
altura_mt=(altura/100)
print(f"Su altura es {altura_mt} m")

#formula
indice_masa_corporal=float(peso/(altura_mt**2))
print(f"Su IMC es {indice_masa_corporal:.2f}\n")

"""
indice_masa_corporal= 18 #para probar condiciones
"""
#Condiciones
if indice_masa_corporal < 18.5:
    print("Clasificación OMS Bajo Peso")

elif indice_masa_corporal >=18.5 and indice_masa_corporal <25:
    print("La clasificacion OMS es: Adecuado")
elif indice_masa_corporal >=25 and indice_masa_corporal <30:
    print("La clasificacion OMS es: Sobrepeso")
elif indice_masa_corporal >=30 and indice_masa_corporal <35:
    print("La clasificacion OMS es: Obesidad Grado I")
elif indice_masa_corporal >=35 and indice_masa_corporal <40:
    print("La clasificacion OMS es: Obesidad Grado II")
elif indice_masa_corporal >=40:
    print("La clasificacion OMS es: Obesidad Grado III")
    

    
