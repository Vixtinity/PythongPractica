#LOS DICCIONARIOS SON SUMAMENTE UTILIZADOS.
punto = {"x": 1, "y":50}
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del(punto["y"])
print(punto)
punto["x"] = 25

#DEVUELVE DUPLAS
for valor in punto.items():
    print(valor)
    
#DEVUELVE DUPLAS
for llave, valor in punto.items():
    print(llave, valor)
    
    

usuarios = [
    {"id": 1, "nombre":"ismael"},
    {"id": 2, "nombre":"felipe"},
    {"id": 3, "nombre":"jose"},
    {"id": 4, "nombre":"maria"},
]

for usuario in usuarios:
    print(usuario["nombre"])
