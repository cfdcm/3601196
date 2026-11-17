# OR
# menu:

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

if opcion == "salchipapa" or opcion == "hamburguesa" or opcion == "arepa":
    print("Compra donde la mona..")
elif opcion == "arroz_huevo" or opcion == "arepa_pollo" or opcion == "calentao":
    print("Compra donde el mocho")
elif opcion == "buñuelos":
    print("Compra los del barrio..")
else:
    print("No tenemos de eso...")

