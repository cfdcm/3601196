# OR
# menu:
dinero = input("Tiene dinero? S/N: ").upper()
opcion = input("""Que quiere desayunar?
    Donde la mona:
        salchipapa
        hamburguesa
        arepa
    Donde el mocho:
        arroz_huevo
        arepa_pollo
        calentao
    En el barrio:
        buñuelos
    : """).lower()

if dinero == "S" and (opcion == "salchipapa" or opcion == "hamburguesa" or opcion == "arepa"):
    print("Compra donde la mona..")
elif dinero == "S" and (opcion == "arroz_huevo" or opcion == "arepa_pollo" or opcion == "calentao"):
    print("Compra donde el mocho")
elif dinero == "S" and opcion == "buñuelos":
    print("Compra los del barrio..")
else:
    print("No tenemos de eso...")

