#Definicion kwargs: permite recibir varios argumentos con clave-valor
def get_products(**products):
    print(products["id"], products["nombre"])
    
#Siempre hay que nombrar los argumentos
get_products(id="10", nombre="Camisa", precio=20.5)
