palabra = input("Ingrese su palabra ")
List = []
List = list(palabra)
print(List)
cont = 0
for i in range(len(List)):
    if(List[i]=="a" or List[i]=="e" or List[i]=="i" or List[i]=="o" or List[i]=="u" or List[i]=="A" or List[i]=="E" or List[i]=="I" or List[i]=="O" or List[i]=="U"):
        cont +=1

print("Su palabra tiene: " , cont , " vocales")