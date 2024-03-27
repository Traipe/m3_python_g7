#PRUEBA DE UNA FORMA, INDIVIDUAL y más reducida

# Lista de recordatorios
recordatorios = [
    ['2021-01-01', '11:00', 'Levantarse y ejercitar'],
    ['2021-01-02', '06:00', 'Empezar el año'],
    ['2021-07-16', '13:00', 'No hacer nada es feriado'],
    ['2021-09-18', '16:00', 'Ramadas']
]

# 1. Agregar un evento el 2 de Enero de 2021 a las 6 de la mañana para "Empezar el Año"
nuevo_evento = ['2021-01-02', '06:00', 'Empezar el Año']
recordatorios.append(nuevo_evento)

# 2. Corregir el evento del 15 de Julio para que sea el 16 de Julio
recordatorios[2][0] = '2021-07-16'

# 3. Eliminar el evento del día del trabajo
del recordatorios[3]

# 4. Agregar una cena de Navidad y una cena de Año Nuevo, ambas a las 22 horas
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Mostrar los recordatorios actualizados
print(recordatorios)
