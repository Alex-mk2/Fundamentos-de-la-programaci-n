

#Definicion de funciones

#Funcion que recibe como parametro una palabra y me indica si es palindromo o no
#Dominio: texto
#Recorrido: Booleano, True o false según sea el caso

#Ejemplo de palabras palindromas
#Reconocer, anilina, rallar, ala

def esPalindromo(palabra):
    #Se define un iterador
    i = 0
    #Se toma el largo de la palabra menos un elemento 
    largoPalabra = len(palabra) - 1
    #Se recorre a traves de while (aun no for), mientras sea menor al largo de texto
    #Y largoPalabra sea mayor a 0
    while(i < len(palabra) and largoPalabra >= 0):
        #Si el palabra[i] distinto a palabra[j]
        if(palabra[i] != palabra[largoPalabra]): #palabra[0], palabra[1], palabra[2].....palabra[n]
            #Se retorna falso, ya que no es igual
            return False
        #Se incrementa el iterador y disminuye largoPalabra
        i+=1
        largoPalabra-=1
    #Retorna verdadero en el caso de que ambas Palabras sean iguales
    return True


#Traza  de la operacion (funcion)

#palabra = ala -----> palabra[0] = a, palabra[1] = l, palabra[2] = a
#i = 0, 1, 2
#largoPalabra = al #largoPalabra = 
#

#Funcion------> argumento --------> (cualquier cosa)------> (lista, entero, booleano, floante)



#Menu principal, donde se realiza llamado de funciones y entradas

palabra = str(input("Ingrese una palabra: "))

palindromo = esPalindromo(palabra)

if(palindromo == True):
    print("Es palindromo")
else:
    print("No es palindromo")