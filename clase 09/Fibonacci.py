

fibonacci = int(input("Ingrese un numero: "))
sumaFibonacci = 0

#Valores de la serie
F = 0
F1 = F2 = 1
i = 2

if(fibonacci == 0 or fibonacci == 1):
    sumaFibonacci = 0
else:
    while(i <= fibonacci):
        #print("Los valores de la serie son: ",i, F, F1, F2)
        F = F1 + F2
        F2 = F1
        F1 = F
        i = i + 1
        if(F > fibonacci):
            break
        print(F)



