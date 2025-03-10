
#Descripcion de funciones

#Descripcion: Funcion que entrega una palabra codificada 
#Dominio: frase
#Recorrido: frase codificado


#Fin descripcion funciones


#Inicio operacion

def codificarPalabra(frase):
    #Hay que separar las palabras con split
    palabras = frase.split() #split permite separar las palabras, ejemplo: "hola"----> split---> "h" "o" "l" "a"
    largoPalabras = len(palabras) #Largo de las palabras
    #Se crea una variable vacia
    codificada = ""
    #Se crea un iterador
    i = 0

    #Mietras sea menor que el largo de palabras
    while(i < len(palabras)):
        #Obtenemos el largo de la palabra
        largo = len(palabras[i]) 
        #Se obtiene la posicion de la palabra
        posicion = largoPalabras % largo 
        #Se concatena la palabra
        codificada += palabras[i][posicion] 
        #Se incrementa iterador
        i = i + 1

    return codificada



#traza de la funcion
#i = 0
#frase = hi---Posiciones!
#largoPalabras = len(palabras) = "h" "i"----> 2 % 1
#Resultado: "h"2 



#Segunda iteracion
#i = 1
#frase = hi----> ""
#largo = len(palabras[1]]) = "i"-----> 1
#2 % 1 = 2
#Resultado:"i"2


#tercera iteracion
#i = 2
#frase = hi
#largo = len(palabras[2])
#Resultado: "h"2 "i"2

#Operaciones menu principal


frase = str(input("Ingrese la frase a codificar: "))

codificar = codificarPalabra(frase)

print("La palabra codificada es:", codificar)
