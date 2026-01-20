mascotas = ["perro", "gato", "loro", "pez"]
print(mascotas[0], mascotas[3])
mascotas[0] = "y tal"
print(mascotas)
print(mascotas[:3])
print(mascotas[-1])
#toma los cares saltando de dos en dos
print(mascotas[::2])
print(mascotas[1::2])


#toma los numeros impares
numeros = list(range(1,21))
#empieza desde el indice 0 que es 1
print(numeros[::2])
#empieza desde el indice 1 que es 2
print(numeros[1::2])
