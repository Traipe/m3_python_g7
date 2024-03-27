#conversiones, forma individual de prueba, más reducida, como referencia

import sys

# Paso 1: Obtener las tasas de conversión y el valor en pesos chilenos desde sys.argv
tasas_conversion = {
    'Sol': float(sys.argv[1]),
    'Peso_Argentino': float(sys.argv[2]),
    'Dolar_Americano': float(sys.argv[3])
}
valor_pesos_chilenos = float(sys.argv[4])

# Paso 2: Calcular el equivalente en las tres monedas y mostrar el resultado
equivalente_soles = valor_pesos_chilenos * tasas_conversion['Sol']
equivalente_pesos_argentinos = valor_pesos_chilenos * tasas_conversion['Peso_Argentino']
equivalente_dolares = valor_pesos_chilenos * tasas_conversion['Dolar_Americano']

print(f"Los {valor_pesos_chilenos} pesos equivalen a:")
print(f"{equivalente_soles} Soles")
print(f"{equivalente_pesos_argentinos} Pesos Argentinos")
print(f"{equivalente_dolares} Dólares Americanos")
