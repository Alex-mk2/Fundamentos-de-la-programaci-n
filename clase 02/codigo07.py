

#Construir un programa en python que imprima de mayor a menor tres numeros ingresados 


#Inicio del programa

#Ingreso de los numeros

numero = int(input("Ingrese el primer numero: "))

#Segundo numero

numero2 = int(input("Ingrese el segundo numero: "))

#Tercer numero

numero3 = int(input("Ingrese el tercer numero: "))


#Definimos variables maxima

max = 0
max2 = 0
max3 = 0


#Se realizan las comparaciones

if(numero >= numero2 and numero >= numero3):

    #Se guarda el numero mayor en este caso
    max = numero #Es el maximo! 

    #Ahora si el numero2 es mayor al 3
    if(numero2 >= numero3):
        #Se guarda el maximo de cada numero
        max2 = numero2 #Segundo numero maximo 
        max3 = numero3 #Tercer candidato maximo
    else:
        #El numero 3 seria  el segundo maximo en caso de que no sea el 2
        max2 = numero3 #El numero3 es el segundo maximo
        max3 = numero2 #El numero2 es el tercer maximo


#Traza para el programa
#numero = 3, max = 3
#numero2 = 2, max2 = 2
#numero3 = 1, max3 = 1




#Segundo caso, cuando el numero dos es mayor
elif(numero2 >= numero and numero2 >= numero3):
    max = numero2 #

    if(numero >= numero3):
        #En este caso el primer numero queda como maximo, luego el 3
        max2 = numero
        max3 = numero3

    else:
        #Caso contrario, numero 3 seria el segundo maximo
        max2 = numero3
        max3 = numero

    
#Tercer caso, cuando ya el numero3 es mayor que todos
else:
    max = numero3 #Maximo seria numero 3

    if(numero >= numero2):
        #El segundo maximo seria numero 1
        max2 = numero
        max3 = numero2
    else:
        #Maximo seria numero 2
        max2 = numero2
        max3 = numero

print("Los numeros ordenados de mayor a menor son: ", max, max2, max3)


#Hacer este mismo ejercicio, pero ordenado de menor a mayor.
#Ejemplo: 1 2 3
#Pista: Revisa la logica de este programa, si por ejemplo aquí se busca el maximo, ahí debes alterar para solo buscar el minimo
#Pista2: cambiar el signo de mayor igual