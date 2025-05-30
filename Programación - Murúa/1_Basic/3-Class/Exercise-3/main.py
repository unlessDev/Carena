# Realice un algoritmo que:
# Permite ingresar una serie de números enteros entre 1 y 999.
# Salir con cero (0).
# Validar que no se ingresen valores fuera del rango y mostrar un mensaje “Valor fuera de rango”.
# Contar y acumular los menores o igual a 500.
# Contar y acumular los valores mayores a 500.
# Mostrar los resultados.

###
# Para este ejercicio tendría que crear una lista de resultados, almacenarlos y compararlos.
###

print("ingresar una serie de números enteros entre 1 y 999")
print("Presione 0 para finalizar...")

maximo = -1  # Inicializamos con un valor menor que todos los posibles

menor = mayor = 0


while True:
    a = int(input("Ingrese el valor: "))
    
    if a == 0:
        break  # Salimos del bucle
    
    if a < 0 and a > 999 :
        print("Valor fuera de rango...")
        continue
    
    if a > maximo:
        maximo = a

# Mostramos el resultado
if maximo == -1:
    print("No se ingresaron números válidos.")
else:
    print(f"El mayor valor ingresado fue: {maximo}")

print("Fin del programa")