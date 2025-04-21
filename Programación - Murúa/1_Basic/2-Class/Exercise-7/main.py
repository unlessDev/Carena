# Desarrollar un algoritmo para calcular las tablas de multiplicar del 1 al 10 en el rango de 1 a 10.
# Mostrar una leyenda de lo que realiza el programa.
# Inicializar las variables que vaya a utilizar como contador y tabla de multiplicar.
# Solicitar al usuario que indique qué tabla se debe calcular.
# Construir un bucle while para iterar y mostrar el resultado de la tabla.
# Utilizar un contador para controlar los ciclos o vueltas.
# Mostrar una leyenda de final del programa.

# Algoritmo para calcular tablas de multiplicar
print("Este programa calcula las tablas de multiplicar del 1 al 10")

# Solicitar al usuario qué tabla desea calcular
while True:
    try:
        tabla = int(input("Ingrese qué tabla desea calcular (1-10): "))
        if 1 <= tabla <= 10:
            break
        else:
            print("¡Error! Debe ingresar un número entre 1 y 10")
    except ValueError:
        print("¡Error! Debe ingresar un número entero válido")

# Mostrar la tabla seleccionada
print(f"\nTabla de multiplicar del {tabla}:")

# Inicializar contador
contador = 1

# Construir bucle while para mostrar la tabla
while contador <= 10:
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")
    contador += 1

# Mensaje final
print("\nFin del programa. ¡Gracias por usar el calculador de tablas!")