import math

try:
    catA = float(input("Ingrese el valor del cateto A: "))
    catB = float(input("Ingrese el valor del cateto B: "))
    C = math.sqrt(catA ** 2 + catB ** 2)
    print(f"\nLa hipotenusa es: {round(C, 2)}")  # Redondeado a 2 decimales
except ValueError:
    print("Error: Si te sale esto, es porque no ingresaste un numero entero")