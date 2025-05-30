# Desarrollar un algoritmo para calcular el promedio de una serie de valores enteros.
# Construir un bucle while para iterar el ingreso de valores.
# Leer el valor ingresado por el usuario.
# Salir cuando el usuario ingrese 0 (cero).
# Validar que el valor esté en el rango de 10 y 99 inclusivos, de lo contrario sacar un mensaje y solicitar nuevo ingreso.
# Contar el valor ingresado.
# Acumular el valor ingresado en la variable acumulador.
# Mostrar los resultados por pantalla.
# Mostrar un mensaje de fin de programa.

print("Calculadora de promedio de valores (10-99)")
print("Ingrese números enteros entre 10 y 99 (ingrese 0 para finalizar)\n")

contador = 0
acumulador = 0

while True:
    try:
        valor = int(input("Ingrese un valor (10-99) o 0 para terminar: "))
        
        if valor == 0:
            break
        
        if 10 <= valor <= 99:
            contador += 1
            acumulador += valor
        else:
            print("¡Error! El valor debe estar entre 10 y 99\n")
            
    except ValueError:
        print("¡Error! Debe ingresar un número entero válido\n")

if contador > 0:
    promedio = acumulador / contador
    print("\n" + "="*40)
    print(f"Total de valores ingresados: {contador}")
    print(f"Suma total de valores: {acumulador}")
    print(f"Promedio calculado: {promedio:.2f}")  # Mostrar con 2 decimales
    print("="*40)
else:
    print("\nNo se ingresaron valores válidos para calcular el promedio")

print("\nFin del programa. ¡Gracias por usar la calculadora!")