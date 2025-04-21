# Tomar como partida el ejercicio 7 y hacer las siguientes modificaciones.
# Agregar un bucle while más externo que contenga desde el input de pedido de número de tabla hasta la instrucción previa a la leyenda de fin de programa.
# Salir del programa cuando el usuario de Enter sin ingresar ningún valor para la tabla.

# Algoritmo para calcular tablas de multiplicar con bucle externo
print("Este programa calcula las tablas de multiplicar del 1 al 10")
print("Presione Enter sin ingresar valor para salir\n")

while True:
    # Solicitar al usuario qué tabla desea calcular
    entrada = input("Ingrese qué tabla desea calcular (1-10) o Enter para salir: ")
    
    # Salir si el usuario presiona Enter sin ingresar valor
    if entrada == "":
        break
    
    try:
        tabla = int(entrada)
        if 1 <= tabla <= 10:
            # Mostrar la tabla seleccionada
            print(f"\nTabla de multiplicar del {tabla}:")
            
            # Inicializar contador
            contador = 1
            
            # Construir bucle while para mostrar la tabla
            while contador <= 10:
                resultado = tabla * contador
                print(f"{tabla} x {contador} = {resultado}")
                contador += 1
                
            print()  # Línea en blanco para separar
        else:
            print("¡Error! Debe ingresar un número entre 1 y 10\n")
    except ValueError:
        print("¡Error! Debe ingresar un número entero válido\n")

# Mensaje final
print("Fin del programa. ¡Gracias por usar el calculador de tablas!")