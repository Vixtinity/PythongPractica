#con DEF ORDENAR ordeno por el indice 1, que esn este caso es el id
usuarios2 = [
    ["Juan", 10], 
    ["Ana", 3], 
    ["Pedro", 2]
    ]
#para usar lamba hay que pasarle dos elementos, parametros:valorRetorno
#FUNCIONES ANONIMAS
#Usar las funciones anonimas solo cuando esa funciona SOLO se vaya a usar en esa parte del codigo y no se vuelva a usar
usuarios2.sort(key=lambda el:el[1], reverse=False)
print(usuarios2)
