numeros = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]
#NO HACER ESTO
#primero = numeros[0]
#segundo = numeros[1]
#tercero = numeros[2]

#Tomo todos
primero, segundo, tercero, cuarto, quinto, sexto, septimo, octavo, noveno, decimo = numeros
print(primero, segundo, tercero, cuarto, quinto, sexto, septimo, octavo, noveno, decimo)

#tomo el primer elemento y los demas se guardan en resto que es iterable
primero2, *resto = numeros
print(primero2)

#tomo los dos primeros
primero3, segundo3, *resto3 = numeros
print(primero3, segundo3, resto3)

#tomo el primer y ultimo elemento
primero4, *resto4, ultimo4 = numeros
print(primero4, ultimo4, resto4)