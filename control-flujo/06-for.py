#iterar

#imprime 5 veces
buscar = 3
#range 5 es un iterable
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break

for char in "Ultimate Python":
    print(char)