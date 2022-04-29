while True:
    try:
        a = int(input("Ingrese el numero a"))
        b = int(input("Ingrese el numero b"))
        c = a + b
        print("La suma de estos dos numeros es: ",c)
        continue
    except Exception as exc:
        print("Algun Ingreso no es numerico, Intente de nuevo... ")
