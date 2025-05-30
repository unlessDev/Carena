# Tomar como partida el ejercicio 7 y hacer las siguientes modificaciones.
# Agregar un bucle while más externo que contenga desde el input de pedido de número de tabla hasta la instrucción previa a la leyenda de fin de programa.
# Salir del programa cuando el usuario de Enter sin ingresar ningún valor para la tabla.

# Algoritmo para calcular tablas de multiplicar con bucle externo
print("Este programa calcula las tablas de multiplicar del 1 al 10")
print("Presione Enter sin ingresar valor para salir\n")

while True:
    entrada = input("Ingrese qué tabla desea calcular (1-10) o Enter para salir: ")
    
    if entrada == "":
        break
    
    try:
        tabla = int(entrada)
        if 1 <= tabla <= 10:
            print(f"\nTabla de multiplicar del {tabla}:")
            
            contador = 1
            
            while contador <= 10:
                resultado = tabla * contador
                print(f"{tabla} x {contador} = {resultado}")
                contador += 1
                
            print()
        else:
            print("¡Error! Debe ingresar un número entre 1 y 10\n")
    except ValueError:
        print("¡Error! Debe ingresar un número entero válido\n")

print("Fin del programa. ¡Gracias por usar el calculador de tablas!")