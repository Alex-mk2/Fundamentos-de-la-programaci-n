#Ejercicio para saber si una palabra es palindromo o no

texto = str(input("Ingrese un texto: "))

i = 0

#Largo del texto = (cantidad totales de letras) - 1
largoTexto = len(texto) - 1

flag = False

#Logica de procesar el palindromo
while(i < len(texto) and largoTexto >= 0): #3 < 3 F and -1 >= 0 F------------->condicion falsa
    if(texto[i] != texto[largoTexto]): #texto[2] = 'a', texto[0] = 'a'
        flag = False
    else:
        flag = True #cuando ambas palabras sean iguales tanto de izquierda como de derecha y viceversa
    i = i + 1
    largoTexto = largoTexto - 1


#Condicion de bandera
if(flag == True): #True------------> palabra = ala si es palindroma
    print("Es palindromo")
else:
    print("No es palindromo")



#Traza del programa
#texto = 'ala'-------> 'a'[0] 'l'[1] 'a'[2]
#len(texto) = 3
#i = 0
#largoTexto = 3 - 1 = 2
#flag = False

#*****************Estado inicial*****************************


#Traza del programa
#texto = 'ala'-------> 'a'[0] 'l'[1] 'a'[2]
#len(texto) = 3
#i = 1
#largoTexto = 2 - 1 = 1
#flag = Verdadera

#***********Segunda iteracion*****************

#Traza del programa
#texto = 'ala'-------> 'a'[0] 'l'[1] 'a'[2]
#len(texto) = 3
#i = 2
#largoTexto = 1 - 1 = 0
#flag = Verdadera



#*********Tercera iteracion****************
#Traza del programa
#texto = 'ala'-------> 'a'[0] 'l'[1] 'a'[2]
#len(texto) = 3
#i = 3
#largoTexto = 0 - 1 = -1
#flag = Verdadera