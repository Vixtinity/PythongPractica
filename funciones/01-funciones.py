#con def defino funciones
#NOMBRE Y APELLIDO SON PARAMETROS!!!
def hola(nombre, apellido):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")

#aqui le paso el valor ismael a hola (ARGUMENTO)
hola("ismael", "fernandez")

#hay que nombrar todos los argumentos
hola(apellido="fernandez", nombre="ismael")
