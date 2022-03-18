
def EncontrarCapicua(a):

    b = "".join(reversed(a))
    if(a == b):
        return "Es capicua"

    else:
        return "No es capicua"   

while(True):

    a = input("Ingrese una palabra y le diremos si es Capicua, Para terminar ingrese T\n")
    if( a == "T" or a == "t"):
        break
    else:
        print(EncontrarCapicua(a))


