
#Definicion de funciones

#Descripcion de funciones: una funcion que traduce de lenguaje natural a ladron
#Dominio: texto (string)
#Recorrido: texto (string)

#Definicion de constantes
CONSONANTES = "abcdfghjklmnpqrstvwxyz"

#Fin definicion constantes


#Fin def funciones


#Inicio operatoria

def traducirALenguajeLadron(texto):
    #Se crea una variable a traducir
    traducir = ""
    #Se crea un iterador
    i = 0
    #Mientras no alcance el largo de la palabra
    while(i < len(texto)):
        #Se toma cualquier palabra, ya que ira cambiando con el iterador
        caracter = texto[i] 
        if(caracter in CONSONANTES): #Si esta en la constante consonantes
            traducir = traducir + caracter + "o" + caracter 
        else: #Caso que no se encuentre en consonantes
            traducir = traducir + caracter
        #Se incrementa iterador
        i = i + 1
    return traducir

#Fin operatoria de funciones


#Traza de la funcion

#Primera iteracion
#i = 0
#texto = hola
#caracter = texto[i] = h, condicion verdadera,
#Operacion: traducir = "" + h + "o" + "h"------> traducir = hoh

#Segunda iteracion
#i = 1
#texto = hola
#caracter = texto[i] = o
#Operacion: #traducir = "hoh" + "o" + "o"
#traducir: hohoo

#Tercera iteracion
#i = 2
#texto = hola
#caracter = texto[i] = l
#Operacion: #traducir = hohoo + "l" + "o" + "l"-----> traducir = hohoolol

#Cuarta iteracion
#i = 3
#texto = hola
#caracter = texto[i] = a
#Operacion: #traducir = hohoolol + "a" + "o" + "a"------>traducir = hohoololaoa


#Quinta iteracion 
#i = 4
#texto = hola
#caracter = texto[i] = ''
#traducir = hohololaoa

#Menu principal para ingresar la palabra y llamado de funciones

palabra = str(input("Ingrese una palabra: "))

traducir = traducirALenguajeLadron(palabra)


print("El texto traducido a lenguaje ladron es: ", traducir)




