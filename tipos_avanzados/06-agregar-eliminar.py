mascotas = [
    "perro",
    "loro",
    "gato", 
    "loro", 
    "pez"
]
#con insert me permite agrega la posicion, y append lo agrega al final
mascotas.insert(1, "tortuga")
mascotas.append("hamster")
print(mascotas)

#elimina solo el primero
mascotas.remove("loro")
print(mascotas)

#borra el elemento que pertenece al indice
mascotas.pop(1)
print(mascotas)

del mascotas[2]
print(mascotas)

#borra todo
mascotas.clear()
print(mascotas)