usuarios = [
    ["Juan", 10], 
    ["Ana", 3], 
    ["Pedro", 2]
    ]

#nombres = [] 
#for usuario in usuarios:
#    nombres.append(usuario[0])
#print(nombres)

#expresion es la transformacion que le vamos a aplicar
#Transformacion - map
nombres = [usuario[0] for usuario in usuarios]
print(f"Transformacion: {nombres}")

#Filtrar
#filtro los usuarios si su id es mayor a 2
#Ahora filtra y transdorma la lista - filter
#al forma sugeria es usar las listas de compresion pero quizas es necesario map y filter
nombres2 = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(f"Filtro y transformacion: {nombres2}")

#map
nombre3 = list(map(lambda usuario: usuario[0], usuarios))
print(f"Filter: {nombre3}")

#filter
nombre4 = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(f"Filter: {nombre4}")

