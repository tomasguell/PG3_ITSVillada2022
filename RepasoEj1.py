


def BuscarNum(Lista, NumBuscado):
    try :
        result = Lista.index(NumBuscado)
        return result
    except ValueError:
        return ("El valor no se encuentra en la lista  ")
    




Lista = [1,2,13,14,18,60,86]
print(Lista)
flag = 1
NumBuscado = 0
while(flag == 1):
    NumBuscado = int(input("Ingrese el numero a buscar  "))
    print(BuscarNum(Lista, NumBuscado))
    b = int(input("  Presione cualquier otro numero para seguir \n 2:no \n"))
    if (b == 2):
        flag = 0
    
    

