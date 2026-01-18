NOMBRE = "Ismael"
APELLIDO = "Fernandez"
#No es la mejor forma
NOMBRE_COMPLETO = NOMBRE + " " + APELLIDO
print(NOMBRE_COMPLETO)
#f es para formatear strings siempre que esten dentro de un f podemos poner lo que queramos
NOMBRE_COMPLETO_BIEN = f"{NOMBRE} {APELLIDO}"

NOMBRE_PRUEBA = f"{NOMBRE.upper()} {2+5}"

print(NOMBRE_COMPLETO_BIEN)
print(NOMBRE_PRUEBA)
