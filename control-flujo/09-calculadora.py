print("Bienvenido")
print("Para salir escribe salir")
print("Operaciones: suma, resta, multi, div")

n1 = ""
while True:
    if not n1:
        n1 = input("Primer numero:")
        if n1.lower() == "salir":
            break
    n1 = int(n1)

    op = input("Operacion:")
    if op.lower() == "salir":
        break

    n2 = input("Segundo numero:")
    if n2.lower() == "salir":
        break

    n2 = int(n2)
    if op == "suma":
        n1 += n2

    elif op == "resta":
        n1 -= n2

    elif op == "multi":
        n1 *= n2

    elif op == "div":
        n1 /= n2

    else:
        print("Operacion no reconocida")
        break
    print("Resultado:", n1)
