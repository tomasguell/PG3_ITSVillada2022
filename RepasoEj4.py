Lista =[]
while(True): 

    NumeroIngresado = input("Ingrese el numero que quiere agregar, para terminar ingrese T \n")
    if( NumeroIngresado == "T" or NumeroIngresado == "t"):
        break
    else:
        Lista.append(int(NumeroIngresado))
        print(Lista)


print(sorted(Lista, reverse= True))