n1 = input("Ingrese el primer numero: ")
n2 = input("Ingrese el segundo numero: ")

n1 = int(n1)
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2
#f es importante para formatear strings
mensaje= f"""
Resultado de la suma: {suma}
Resultado de la resta: {resta}
Resultado de la multiplicacion: {multiplicacion}
Resultado de la division: {division}
"""

print(mensaje)
