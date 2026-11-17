conexion = input("Hay coneción con MySQL ? S/N: ").upper() in {'S', 'Y'}

# shortcuts

if not conexion:
    print("No hay conexión....")
else:
    print("Conexión OK")
