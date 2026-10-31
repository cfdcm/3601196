# operador in: buscar aguja en pajar, para capturar boleanos.

#                                   conjunto: set
estudio = input("Estudió S/N: ").lower() in {"s", "si"}
print(f"Estudió?: {estudio}")

es_casado = input("Estado civil Soltero/Casado: ").upper() in {"SOLTERO", "CASADO"}
print(f"Es casado?: {es_casado}")


