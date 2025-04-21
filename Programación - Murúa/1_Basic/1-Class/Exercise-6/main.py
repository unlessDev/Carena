#Desarrollar un algoritmo para mostrar la tabla de multiplicar por 3 desde el 1 al 10 (no pedir ingreso de datos).
#Mostrar mensaje, ej : “1 x 3 = ”
#Mostrar el resultado de la multiplicación 1 x 3 al lado del igual dejando un espacio.
#Repetir hasta el 10 (usar solo instrucciones conocidas hasta ahora).

print("Tabla del 3")
print()

for i in range(0, 11):
    print(f"{i} x 3 = {i*3}")