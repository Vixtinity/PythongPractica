mascotas = ["perro", "gato", "loro", "pez"]

#enumarte devuelve el valor y el indice.
#SE LE LLAMA TUPLA [(0, "perro"), (1, "gato")]
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)