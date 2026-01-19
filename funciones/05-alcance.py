#contexto global MALA PRACTICA!!
saludo = "Hola global"

def saludar():
    saludo = "Hola"
    print(saludo)
    
def saludar2():
    #la variable saludo no existe en este ambito
    saludo = "y tal"
    print(saludo)
    
saludar()
saludar2()
saludar()
print(saludo)
