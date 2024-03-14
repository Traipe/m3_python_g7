precio = input("Ingrese el precio de suscripción en CLP:")
precio = float(precio)

usuarios = input("Ingrese el número de usuarios normales \n:")
usuarios = int(usuarios)

usuarios_premium = input("Ingrese el número de usuarios premium \n:")
usuarios_premium = int(usuarios_premium)

gasto_total = float(input("Ingrese los gastos totales en CLP \n:"))
gasto_total = float(gasto_total)

utilidades = (precio * usuarios)+ (precio*1.5*(usuarios_premium)) - gasto_total
print("las utilidades son {utilidades}CLP")
                                   