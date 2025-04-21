# Desarrollar un algoritmo para determinar el mayor de tres números distintos.
# Muestra un mensaje de presentación.
# Mostrar mensaje de ingreso de un valor y guardarlo en la variable a.
# Mostrar mensaje de ingreso de un valor y guardarlo en la variable b.
# Mostrar mensaje de ingreso de un valor y guardarlo en la variable c.
# Implementar tres comparaciones para determinar cuál es el mayor.
# Mostrar el mensaje correspondiente para cada resultado de la comparación.
# Mostrar Fin del programa.

print("Ingrese 3 valores enteros para verificar cual es el de mayor valor...")

a = int(input("1er valor: "))
b = int(input("2do valor: "))
c = int(input("3er valor: "))

if a == b or b == c or a == c:
    print("Error: Los valores deben ser distintos, no repetirse.")
else:
    if a > b and a > c:
        print("El mayor es:", a)
    elif b > c:
        print("El mayor es:", b)
    else:
        print("El mayor es:", c)

print()
print("Fin del programa")