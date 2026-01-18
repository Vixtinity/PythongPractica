edad=int(input("Cual es tu edad?\n"))

if edad > 17 and edad < 55:
    print("Puede ver la pelicula")
elif edad >= 55 and edad < 60:
    print("Tienes un descuento")
elif edad >= 60:
    print("Superdescuento")
else:
    print("No puedes entrar")
print("Listo")