

#Ejercicio n°8, construya un programa en python que cuente cuantas veces se repite una letra 


#Inicio del programa

#Ingresar string por pantalla

frase = str(input("Ingrese una frase: "))

#Ingresar la letra que se quiere buscar
letra = str(input("Ingrese una letra a contar: "))

#Se crea un contador
contador = 0

#Se crea un iterador
iterador=0




#Traza para el programa
#Frase = 'hola'---->Lista de string----->'h = L[0]', 'o = L[1], 'l = L[2], 'a = L[3]'----> len(4)
#letra = 'l'
#iterador = 0, 1, 2, 3, 4
#contador = 0, 1, contador = 1


#Ejecicion del if
#frase[0] = h, letra = l, frase == letra (h != l)
#frase[1] = o, letra = l, frase == letra (o != l)
#frase[2] = l, letra = l, frase == letra (l == l)
#frase[3] = a, letra = l, frase == letra (a != l)
#Fin de la ejecucion if

#Mientras sea menor que el largo de la frase
while(iterador < len(frase)): 

    #En caso de que se haya encontrado la letra
    if(frase[iterador] == letra): 
        #Incrementamos el contador
        contador= contador + 1
    iterador= iterador + 1

print("La cantidad de veces que aparece esta letra es:", contador)