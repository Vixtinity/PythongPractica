def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    comparacion = texto[::-1]
    if texto == comparacion:
        return True
    else:   
        return False
    

    

print("Abba", es_palindromo("Abba"))