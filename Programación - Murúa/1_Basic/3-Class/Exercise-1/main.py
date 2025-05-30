# Generar una serie de 20 números al azar de hasta 3 dígitos.
# Importar la biblioteca random (import random).
# Generar números aleatorios entre 100 y 999 (random.randint(100, 999).
# Contar y acumular los divisibles por 2 (operador módulo %).
# Contar y acumular los divisibles por 3.
# Contar y acumular los divisibles por 4. 
# Contar y acumular los divisibles por 5. 
# Mostrar los resultados al finalizar el bucle.

import random

# Generar la lista de números aleatorios
numeros = [random.randint(100, 999) for _ in range(20)]

# Inicializar contadores
div2 = div3 = div4 = div5 = 0

# Recorrer la lista de números y contar los divisibles
for num in numeros:
    if num % 2 == 0:
        div2 += 1
    if num % 3 == 0:
        div3 += 1
    if num % 4 == 0:
        div4 += 1
    if num % 5 == 0:
        div5 += 1

# Mostrar resultados
print("Lista de números generados:", numeros)
print(f"Divisibles por 2: {div2}")
print(f"Divisibles por 3: {div3}")
print(f"Divisibles por 4: {div4}")
print(f"Divisibles por 5: {div5}")