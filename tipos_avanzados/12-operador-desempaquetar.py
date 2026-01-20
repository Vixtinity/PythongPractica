lista = [1, 2, 3, 4]
#print(*lista)

#DE QUE NOS SIRVE?
#En caso de que tengamos una funciona definida, N por ejemplo, y que reciba los args n1,n2,n3, y que esos 3 args esten en una lista
#llamamos a la funcion N, le pasamos la lsita con el operador de desempaquetamiento *, para que le pase cada elemento para que se los pase cada uno
#como cada uno de sus argumentos

lista2 = [5, 6]
combinada = ["Hola", *lista, "mundo", *lista2]
print(combinada)