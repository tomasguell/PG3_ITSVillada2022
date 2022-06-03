"""Almacenar una serie de string en un archivo de texto. 
Tratar de llamar al método 'write' pasando un entero. 
Capturar la excepcion correspondiente."""


while True:
    completeName = "EjerciciosExceptions/" + "texto" + ".txt"
    file1 = open(completeName, "a")

    try:
        toFile = input("Ingrese lo que quiera ingresar, que sea un STR")

        if toFile.isnumeric() == True:

            file1.write(int(toFile + "\n"))

        else:
            file1.write(toFile + "\n")

        ans = input(
            "Si quiere terminar ingrese [n], si quiere seguir ingrese cualquier otra letra: "
        )
        if ans == "n":
            file1.close()
            break
    except TypeError:
        print("Su ingreso tiene algun tipo de numeros")
