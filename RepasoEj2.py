def AñoBisiesto(Año):
    if(Año%400 == 0 or  Año%4 == 0 and  Año%100 != 0):
        return "El año Ingresado es Bisiesto"
    else:
        return "El año Ingresado no es Bisiesto"    



Año = int(input("Ingrese el año a ser analizado"))
print(Año)
print(AñoBisiesto(Año))