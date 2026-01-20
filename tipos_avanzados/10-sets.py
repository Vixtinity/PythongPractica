# set = grupo o conjunto
# QUE ES UN SET? Coleccion de datos que no se puede repetir y que no esta ordenada
primer = {1, 1, 2, 2, 3, 3}
#TRANFORMAR LISTA A SET
segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)
#Une los sets que los pasamos
# | = UNION
print( primer | segundo)
#& = INTERSECCION
#Solo devuelve los elemento que se encuentre dentro de los dos sets, en este caso es solo el 3
print(primer & segundo)
#El set segundo elimina intenta eliminar del set primer sus elementos
#ES DECIR, si segundo tiene un 3, 4 y 5, y primer tiene 3, ELIMINA 3 del set primer
print(primer - segundo)
#DIFERENCIA SIMETRICA: devuelve los elementos que se encuentres en el primero y el segundo, y elimina los que se compartan entre ambos.
#ELIMINA LOS DUPLICADOS ENTRE SETS
print(primer ^ segundo)

