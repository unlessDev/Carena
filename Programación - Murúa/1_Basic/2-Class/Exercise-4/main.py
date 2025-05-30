# Desarrollar un algoritmo para determinar el mayor de tres números, puede haber iguales.
# Codificar como se muestra en el diagrama de flujo adjunto.

print("Determinaremos el mayor de tres números (pueden haber valores iguales)")

a = int(input("1er valor: "))
b = int(input("2do valor: "))
c = int(input("3er valor: "))

if a >= b and a >= c:
    max = a
elif b >= c:
    max = b
else:
    max = c

cont = 0
if a == max:
    cont += 1
if b == max:
    cont += 1
if c == max:
    cont += 1

if cont == 1:
    print(f"El mayor es: {max}")
else:
    print(f"El mayor es {max} (aparece {cont} veces)")

print("Fin del programa")