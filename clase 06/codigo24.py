#Construir un programa que permita saber si un numero es fuerte o no
#Un número fuerte se define como un número que es igual a la suma del factorial de sus dígitos.


#Definicion de funciones

#Se utilizara una funcion que permita el calculo de un numero fuerte
#Funcion para realizar el calculo de un factorial -----> 5!-----> 5 x 4 x 3 x 2 x 1 = 120
#Funcion que realice la descomposicion de numeros

#Fin de definicion de funciones



#Definicion de constantes

#No hay

#Fin definicion de constantes


#Descripcion: factorial (calculo)
#Dom: numero
#Recorrido: variable

#Procedimiento

def numeroFactorial(numero): #5!-----> 5 x 4 x 3 x 2 x 1
    #Se crea un iterador
    i = 1
    #Se crea una variable resultado
    resultado = 1
    #Mientras sea menor igual al numero
    while(i <= numero):
        #Se genera la secuencia del factorial
        resultado = resultado * i # 2 x 3
        i+=1
    return resultado

#Traza de la funcion
#resultado = 1
#i = 1
#numero = 3

#Segundo ciclo
#i = 2
#resultado = 1, 2
#numero = 3

#tercer ciclo
#i = 3
#resultado = 1, 2, 6
#numero = 3

#cuarto ciclo
#i = 4
#resultado = 1, 2, 6----->resultado = 6 #3!-----> 3 x 2 x 1 = 6
#numero = 3


#Funcion para realizar la descomposicion de digitos
#Dom: numero
#Recorrido: digitos (variable)
 

def descomponerNumeros(numero):
    #Se crea una lista vacia
    digitos = []
    #Se convierte el numero a string
    numero_convertido = str(numero) # '3'
    #Se crea un iterador
    i = 0
    #Mientras no alcance el largo de la lista
    while(i < len(numero_convertido)):
        #Se guarda en la lista digitos
        digitos.append(int(numero_convertido[i]))
        i = i + 1 
    return digitos


#Traza segunda funcion
#numero = 3----> '3'----> len('3') = 1
#i = 0
#digitos = [3]

#Segundo ciclo
#numero = 3----> '3'----> len('3') = 1
#i = 1
#digitos = [3]


#Funcion para saber si es un numero fuerte
#Dom: numero
#Recorrido: variable

def esNumeroFuerte(numero):
    #Se utiliza la funcion descomponer
    digitos = descomponerNumeros(numero)
    #Se crea una variable
    suma_digitos = 0
    #Se crea un iterador
    i = 0
    while(i < len(digitos)):
        #Se hace uso de la funcion factorial
        factorial = numeroFactorial(digitos[i])
        #Se guarda lo obtenido en factorial
        suma_digitos+= factorial
        i = i + 1
    #Si cumple con esta condicion es un numero fuerte
    return suma_digitos == numero #6 == 3


#Tercera traza
#digitos = [3]
#suma_digitos = 6
#i = 0
#factorial = numeroFactorial(digitos[i]) = 6


#Segundo ciclo
#digitos = [3]
#suma_digitos = 6
#i = 1
#factorial = numeroFactorial(digitos[i]) = 6
#Es que no es un numero fuerte

#Menu principal
numero = int(input("Ingrese un numero: "))


#Verificaciones
if (esNumeroFuerte(numero) == False):
    print(f"{numero} es un número fuerte.")
else:
    print(f"{numero} no es un número fuerte.")


    