numeros = [2, 4, 1, 45, 75, 22]

#ordena de menos a mayor MODIFICA LA LISTA ORIGINAL
numeros.sort()
print(numeros)

#ordena de mayor a menor MODIFICA LA LISTA ORIGINAL
numeros.sort(reverse=True)
print(numeros)
#sorted devuelve una LISTA NUEVA, NO MODIFICA LA ORIGINAL
numeros2 = sorted(numeros)
print(numeros2)


usuarios = [[10, "Juan"], [3, "Ana"], [2, "Pedro"]]
#SOLO ORDENA EL PRIMER ELEMENTO, SI EL ID ESTA AL FINAL NO FUNCIONA
usuarios.sort()
print(usuarios)

#con DEF ORDENAR ordeno por el indice 1, que esn este caso es el id
usuarios2 = [["Juan", 10], ["Ana", 3], ["Pedro", 2]]
def ordena(elemento):
    return elemento[1]

usuarios2.sort(key=ordena, reverse=True)
print(usuarios2)
