# Ejercicio 1
"""
Necesito un programa que solicite al usuario el nombre de un producto, el precio unitario (que puede tener decimales), la cantidad de unidades que desea comprar, y si cuenta con una membresía de la tienda (ingresando 'S' o 'N'). El programa debe calcular el costo total de la compra y mostrar un mensaje formateado que indique el valor total a pagar junto con la confirmación de la membresía.
"""
# entradas
nombre_del_producto = input("Digite el nombre del producto: ")
precio = float(input("Precio Unitario: "))
cantidad = int(input("Cantidad a comprar: "))
membresia = input("Cuenta con una membresía S/N: ")

# proceso
total = precio * cantidad

# salida: f-print o f-string        concatenación
print(f"Total de la compra {total}. Tiene membresía?: {membresia}")
