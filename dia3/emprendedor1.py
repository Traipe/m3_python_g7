# Solicitar datos de entrada
precio = input("Ingrese el precio de suscripción en CLP:")
precio = float(precio)
usuarios = input("Ingrese el número de usuarios \n:")
usuarios = int(usuarios)
gasto_total = float(input("Ingrese los gastos totales en CLP \n:"))
gasto_total = float(gasto_total)

utilidades = (precio * usuarios) - gasto_total
print("las utilidades son {utilidades}CLP")

