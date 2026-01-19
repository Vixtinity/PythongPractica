#el astericos permite recibir varios argumentos
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print("La suma es:", resultado)

suma(10,20,20,100,100)
