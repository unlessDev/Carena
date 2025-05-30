# Genera una serie de 30 números al azar de hasta 3 dígitos.
# Importar la biblioteca random (import random).
# Generar números aleatorios entre 0 y 999 (random.randint(0, 999).
# Contar y acumular los valores entre 0 y 300 inclusivos.
# Contar y acumular los valores entre 301 y 600 inclusivos.
# Contar y acumular los valores entre 601 y 1000 inclusivos.
# Mostrar los resultados.

import random

# Generar la lista de números aleatorios
numeros = [random.randint(100, 999) for _ in range(30)]

# Inicializar contadores
acu = acu2 = acu3 = 0

for num in numeros:
    # Contar y acumular los valores entre 0 y 300 inclusivos.
    if num <= 300:
        acu += 1
    # Contar y acumular los valores entre 301 y 600 inclusivos.
    if num >= 301 and num <= 600:
        acu2 += 1
    # Contar y acumular los valores entre 601 y 1000 inclusivos.
    if num >= 601 and num <= 1000:
        acu3 += 1

# Mostrar resultados
print()
print("Lista de números generados:", numeros)
print()
print(f"Total de número acumulados entre los valores 0 y 300: {acu}")
print()
print(f"Total de número acumulados entre los valores 301 y 600: {acu2}")
print()
print(f"Total de número acumulados entre los valores 601 y 1000: {acu3}")