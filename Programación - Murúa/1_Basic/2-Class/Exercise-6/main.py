# Tomando como partida el ejercicio del punto 5 mejorar el algoritmo para que funcione con valores negativos y positivos.
# Definir una variable booleana para establecer el primer valor.
# Considera poner como mayor el primer valor de la serie.
# Salir con cero.

print("Ingrese números enteros. Presione 0 para finalizar.")

maximo = None
contador = 0

while True:
    try:
        a = int(input("Valor: "))
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        continue
    
    if a == 0:
        break
    
    if maximo is None:
        maximo = a
        contador = 1
    elif a > maximo:
        maximo = a
        contador = 1
    elif a == maximo:
        contador += 1

# Resultado
if maximo is None:
    print("No se ingresaron números.")
else:
    print(f"El mayor valor fue {maximo} (apareció {contador} veces)")