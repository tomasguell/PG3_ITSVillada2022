

def isStep(n):
    a = map(int, str(n)[1:]) 
    b = map(int, str(n)[:-1])
    return all(abs(a_digit - b_digit) == 1 for a_digit, b_digit in zip(a, b))



Numero = int(input("Ingrese un numero "))


if(isStep(Numero) == True):
    print("El numero es step")
else:
    print("El numero no es step")    





   

