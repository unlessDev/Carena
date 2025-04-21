# Desarrollar un algoritmo para permitir el ingreso de una serie de números enteros positivos, hasta que el usuario ingrese el número 0, determinar cuál es el mayor.
# Muestre un mensaje de presentación.
# Iniciar una variable mayor en cero para obtener el mayor propiamente.
# Hacer un bucle while que permita ingresar una serie de números enteros.
# Dentro del bucle solicitar el ingreso de un valor entero para a.
# Verificar si el número ingresado es cero para encontrar la salida de bucle con break.
# Verificar si a es mayor que mayor y copiar a en mayor si es verdadero.
# Por la línea siguiente fuera del bucle mostrar un mensaje y el mayor.

print("Ingrese enteros positivos y verificaremos cual de todos es el mayor.")
print("Presione 0 para finalizar y obtener el resultado.")

maximo = -1  # Inicializamos con un valor menor que todos los posibles

while True:
    a = int(input("Valor: "))
    
    if a == 0:
        break  # Salimos del bucle
    
    if a < 0:
        print("¡Solo se permiten positivos! Ingrese otro número.")
        continue
    
    if a > maximo:
        maximo = a

# Mostramos el resultado
if maximo == -1:
    print("No se ingresaron números válidos.")
else:
    print(f"El mayor valor ingresado fue: {maximo}")

print("Fin del programa")