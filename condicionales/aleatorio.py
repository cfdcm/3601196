# aleatorios, azar
from random import randint, choice

num = randint(20, 30)
print(num)

# lanzar dos dados...

dado1 = randint(1, 6)
dado2 = randint(1, 6)

print(f"Dado1: {dado1}, Dado2: {dado2}")

conteo = 0

if dado1 == 1 or dado2 == 1:
    conteo = conteo + 1
else:
    pass

dado1 = randint(1, 6)
dado2 = randint(1, 6)

print(f"Dado1: {dado1}, Dado2: {dado2}")
if dado1 == 1 or dado2 == 1:
    conteo = conteo + 1
else:
    pass

dado1 = randint(1, 6)
dado2 = randint(1, 6)

print(f"Dado1: {dado1}, Dado2: {dado2}")
if dado1 == 1 or dado2 == 1:
    conteo = conteo + 1
else:
    pass


print(f"La cantidad de veces que cayó 1 fue: {conteo}")