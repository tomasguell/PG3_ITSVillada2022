while True:
    try:
        print("vamos a dividir estos numeros ")
        a = int(input("Ingrese el numero a"))
        b = int(input("Ingrese el numero b"))
        c = a / b
        print("La division de estos dos numeros es: ",c)
        continue
    except ValueError as exc:
        print("Uno de los datos Ingresados no es un numero")
    except ZeroDivisionError  as exc:
        print("No se puede dividir por 0, intente de nuevo")
    