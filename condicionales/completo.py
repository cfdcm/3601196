# Condicionales..Completos: if ... elif ... else
#       
#                    si    sino-si   sino
dinero = 50000
desayuno = input("Opciones de desayuno:\n-----------\nHamburguesa\nHuevos\nBuñuelos\nPescado\nEscriba lo que desea: ").upper()
if desayuno == "HAMBURGUESA":
    # anidamiento, condicionacional dentro de otro...
    if dinero > 20000:
        print('Costo: $25.000')
    else:
        print('Costo: $15.000')
elif desayuno == "HUEVOS":
    print("Costo: $9.000")
elif desayuno == "BUÑUELOS":
    print("Costo: $500")
elif desayuno == "PESCADO":
    print("Costo: $25.000")
else:
    print("No tengo de eso...")


# prueba de escritorio ó depuración del código... Run and Debug