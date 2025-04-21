# Desarrollar un algoritmo para determinar el mayor de tres números, puede haber iguales.
# Codificar como se muestra en el diagrama de flujo adjunto.

print("Determinaremos el mayor de tres números (pueden haber valores iguales)")

a = int(input("1er valor: "))
b = int(input("2do valor: "))
c = int(input("3er valor: "))

if a >= b and a >= c:
    maximo = a
elif b >= c:
    maximo = b
else:
    maximo = c

# Contamos repeticiones del máximo
contador = 0
if a == maximo:
    contador += 1
if b == maximo:
    contador += 1
if c == maximo:
    contador += 1

# Resultado
if contador == 1:
    print(f"El mayor es: {maximo}")
else:
    print(f"El mayor es {maximo} (aparece {contador} veces)")

print("Fin del programa")