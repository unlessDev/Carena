# Desarrollar un algoritmo para determinar el mayor de dos números enteros distintos.
# Mostrar un mensaje de presentación explicando que hace el programa.
# Mostrar mensaje de ingreso de un valor y guardarlo en la variable a.
# Mostrar mensaje de ingreso de un valor y guardarlo en la variable b.
# Por la salida del No comprobar Si a > b.
# Por la salida del Sí indicar que a es mayor que b.
# Por la salida del No indicar que b es mayor que a.
# Mostrar Fin del programa.

print("Ingrese 2 valores enteros y verificaremos cual es el de mayor valor...")

a = int(input("1er valor: "))
b = int(input("2do valor: "))

if (a > b):
    print(a , "Es mayor que:", b)
elif (a < b):
    print(b, "Es mayor que:", a)
else:
    print("Ambos valores son iguales...")
    