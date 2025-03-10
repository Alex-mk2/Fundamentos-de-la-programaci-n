#Construccion de una funcion que permita reducir letras adyacentes iguales
#Este programa lo que realiza es eliminar caracteres repetidos

#Un ejemplo de esto es la palabra Mississippi------>Reduce----->M


#Definicion de funciones

#Descripcion: Funcion que permite reducir una palabra
#Dominio: palabra
#Recorrido: palabra ------> me devolvera un string de esa palabra

#Fin definicion de funciones


#Inicio funcion

def reducirPalabra(palabra):
    #Se crea un iterador
    i = 0
    #Mientras no exceda el largo de la palabra - 1
    while(i < len(palabra) - 1):
        #Si la palabra es igual a la palabra siguiente
        if(palabra[i] == palabra[i+1]): #h == ''
            #Se reemplaza por un string vacio
            palabra = palabra.replace(2*palabra[i], "") #Aqui se utiliza la funcion replace que permite
            #Reemplazar algun elemento de un string por otra cosa
            #Se reinicia el iterador
            i = 0 #En el caso de que haya pillado la letra
        else:
            #Se incrementa el iterador
            i = i + 1 #para seguir buscando en el largo de la palabra
    return palabra


#Traza de la funcion

#replace: Reemplazar algun elemento con otro que se quiera agregar



#Primera iteracion
#i = 0
#palabra = hii-------> largo = 3 - 1 = 2
#palabra = hii ------> palabra[0] = h, palabra[1] = i, palabra[2] = i
#palabra[0] = h == palabra[1] = i, falso



#segunda iteracion
#i = 1, i = 0
#palabra = hii
#palabra[1] = i, palabra[2] = i ---------> replace (2*palabra[1], "")
#-------> replace (2 * (i), "")--------> replace('ii', "")-----> " "
#palabra = h ""
#palabra = h

#Tercera iteracion
#i = 0
#palabra = h

#Cuarta iteracion
#i = 1
#palabra =, ' '





#Fin funcion

#Menu principal, deben estar los llamados y valores por pantalla

palabra = str(input("Ingrese una palabra: "))

reducir = reducirPalabra(palabra)

if(reducir == ""):
    print("La palabra esta vacia")
else:
    print("La palabra se redujo a ", reducir)



