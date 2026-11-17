#Ejemplo1. Preguntar la edad a un usuario y decir si puede votar o no. Mayor a 18 años.
# Además si tiene más de 16 años, decir que se puede lanzar como personero.
# opcion 1 =============================================
edad = int(input("Digite su edad: "))
if edad > 18:
    print("Puede votar")
else:
    print("No puede votar")

if edad > 16:
    print("Puede lanzarse a Personero...")

# opcion 2 =============================================
edad = int(input("Digite su edad: "))
if edad > 18:
    print("Puede votar")
else:
    if edad > 16:
        print("Puede lanzarse a Personero...")
    else:
        print("No puede votar")




# Ejemplo 2: averiguar si un número es negativo, cero o positivo.
# Nota: NO USAR: and, or, MOD.

# opcion 1 ============================================= menos óptimo.....
num = int(input("Digite un num: "))
if num > 0:
    print("Es positivo")
if num < 0:
    print("Es negativo")
if num == 0:
    print("Es cero")

# opcion 2 ============================================= ok
num = int(input("Digite un num: "))
if num > 0:
    print("Es positivo")
elif num < 0:
    print("Es negativo")
else:
    print("Es cero")

# opcion 3 ============================================= ok
num = int(input("Digite un num: "))
if num > 0:
    print("Es positivo")
else:
    if num < 0:
        print("Es negativo")
    else:
        print("Es cero")
# opcion 4 el orden de las preguntas==================== ok
num = int(input("Digite un num: "))
if num < 0:
    print("Es negativo")
elif num == 0:
    print("Es ceroo")
else:
    print("Es positivo")

# Ejemplo 3: Desarrolle un algoritmo que permita leer dos números y ordenarlos de menor a mayor, si es el caso.

# opcion 1 =============================================
num1 = int(input("Digite num1: "))
num2 = int(input("Digite num2: "))
if num1 > num2:
    print(f"Número ordenados: {num2}, {num1}")
else:
    print(f"Número ordenados: {num1}, {num2}")

# opcion 2 =============================================
num1 = int(input("Digite num1: "))
num2 = int(input("Digite num2: "))
menor = ""
mayor = ""
if num1 < num2:
    menor = num1
    mayor = num2
else:
    menor = num2
    mayor = num1

print(f"Número ordenados: {menor}, {mayor}")


# openscoco

# Hacer un programa que pueda dibujar una recta, triángulo o un rectángulo.
""" ejemplo:

print("   *\n  * *\n *   *")

print("* * * *\n*     *\n* * * *")

                *
                *
* * * *         *
                *
                *
"""





"""
Solicitar un número y averiguar si es negativo o positivo, si es positivo, averiguar si es par o impar.
Si es negativo averiguar es un -7 o NO.
"""

#Ejercio 1:
"""
Solicitar 3 números y averiguar cuál es el mayor de los tres.
Nota: NO USAR: and, or.
Insertar datos de prueba así:
1   2   3
1   3   2
2   1   3
2   3   1
3   1   2
3   2   1

Si en todos los casos dice que el mayor es el 3, está OK.
Sino corregir su algoritmo
"""