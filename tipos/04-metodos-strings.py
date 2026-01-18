#Que es un metodo? Funcion que se encuentra dentro de un objeto
ANIMAL = "    PeRRo CaChorRo     "
print(ANIMAL.upper())  #Pone todo en mayusculas
print(ANIMAL.lower())  #Pone todo en minusculas
print(ANIMAL.strip().capitalize())  #Pone la primera letra en mayuscula
print(ANIMAL.title()) #Pone la primera letra de cada palabra en mayuscula
print(ANIMAL.strip()) #Elimina los espacios al inicio y al final
print(ANIMAL.lstrip()) #Elimina los espacios al inicio izquierda
print(ANIMAL.rstrip()) #Elimina los espacios al final derecha
#Si tira -1 es que no lo encontro
#Busca la palabra y devuelve la posicion en la que empieza, si no lo encuentra devuelve -1
print(ANIMAL.find("RR"))
print(ANIMAL.replace("RRo", "gata")) #Reemplaza una palabra por otra
print("RRo" in ANIMAL) #Devuelve True o False si la palabra esta o no esta en el string
print("RRo" not in ANIMAL) #Devuelve True o False si la palabra no esta en el string
