

#Definicion de funciones

#Funcion que permite reemplazar una letra con otra letra
#Dominio: palabra X letra X letra2
#Recorrido: la palabra reemplazada

def reemplazarLetra(palabra, letra, letra2):
    #Se define un iterador
    i = 0
    #Se crea una variable para guardar la palabra
    guardarPalabra = ''
    #Mientras no llegue al largo de la palabra
    while(i < len(palabra)):
        #Si es distinta a la letra que se busca reemplazar
        if(palabra[i] != letra): 
            #Se guarda en una nueva variable
            guardarPalabra += palabra[i]
        else:
            #Se guarda con la letra reemplazada
            guardarPalabra+= letra2 
        #Incrementa el iterador
        i+=1
    #Se hace el retorno de la variable que necesitamos
    return guardarPalabra



#Traza para funcion
#letra = a
#letra2 = B
#i = 0, 1, 2
#guardarPalabra = 'holB'
#palabra = 'hola'-----> palabra[0] = h, palabra[1] = o, palabra[2] = l, palabra[3] = a
#len(palabra) = 4


#Primera iteracion
#i = 0
#letra = a, #palabra[0] = h

#Segunda iteracion
#i = 1
#palabra = o, letra = a

#Tercera iteracion
#i = 2
#palabra = l, letra = a

#cuarta iteracion
#i = 3
#palabra = a, letra = a

#quinta iteracion
#i = 4
#retorna guardarPalabra = 'holB'


#Menu principal 
#Llamados a las funciones, ingresos por pantalla, y demás

palabra = str(input('Ingrese una palabra: '))
letra = str(input('Ingrese letra a reemplazar: '))
letra2 = str(input('Ingrese letra para reemplazar: '))

nuevaPalabra = reemplazarLetra(palabra, letra, letra2)

#Se imprime la nuevaPalabra
print(nuevaPalabra)