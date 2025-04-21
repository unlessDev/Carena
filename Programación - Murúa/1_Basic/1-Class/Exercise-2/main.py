#Desarrollar un algoritmo para el cálculo de la hipotenusa:
#Importar la librería math para obtener la raíz cuadrada (import math).
import math

#Mostrar mensaje de ingreso y guardar cateto A en A.
catA = float(input("Ingrese el 1er valor: "))

#Mostrar mensaje de ingreso y guardar cateto B en B.
catB = float(input("Ingrese el 2do valor: "))

#Calcular y guardar hipotenusa en C “C = math.sqrt( pow(A,2) + pow(B,2) )” o “C = math.sqrt(A ** 2 + B ** 2)”
C = math.sqrt( pow(catA,2) + pow(catB,2) )

#Mostrar mensaje con el resultado de C.
print()
print("Resultado final: ", C)


"""
Rafactorizado:

    try:
    catA = float(input("Ingrese el valor del cateto A: "))
    catB = float(input("Ingrese el valor del cateto B: "))
    C = math.sqrt(catA ** 2 + catB ** 2)
    print(f"\nLa hipotenusa es: {round(C, 2)}")  # Redondeado a 2 decimales
except ValueError:
    print("Error: Ingresa solo números.")
"""