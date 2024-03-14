precio = input("Ingrese el precio de suscripción en CLP:")
precio = int(precio)
usuarios = input("Ingrese el número de usuarios \n:")
usuarios = int(usuarios)
gasto_total = input("Ingrese los gastos totales en CLP \n:")
gasto_total = int(gasto_total)

utilidades = (precio * usuarios) - gasto_total

utilidades_aprevio = input("Ingresa las utilidades del año pasado en CLP \n")
utilidades_aprevio = float(utilidades_aprevio)

diferencia = utilidades / utilidades_aprevio

print(f"Las utilidades son {utilidades} CLP")
print(f"La razon entre las utilidades del año pasado y las actuales son de {round(diferencia,2)}")