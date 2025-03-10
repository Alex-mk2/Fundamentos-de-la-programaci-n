#Programa para ingresar 10 numeros por pantalla y con eso obtener sus posiciones


#Primero que todo, se requiere llenar esta lista...

#-*Se requiere una funcion para realizar el llenado de la lista
#-*Otra funcion para obtener posicion de los elementos

#***************************Implementacion de funciones************************************#

#Funcion que permite el llenado de la lista
#Dom: lista vacia
#Rec: lista con elementos

def llenarLista():
    lista_aux = []
    while(len(lista_aux) < 10):
        numero = int(input("Ingrese un numero a la lista: "))
        lista_aux.append(numero)
    return lista_aux


#Funcion para obtener los elementos de acuerdo a su posicion
#Dom: lista llena X numero
#Rec: elemento lista

def obtenerPosicion(lista, numero):
    i = 0
    posicion = []
    #Se recorre cada elemento de la lista
    while(i < len(lista)):
        if(lista[i] == numero):
            posicion.append(i) #indice
        i = i + 1
    return posicion


#Ejecucion del programa


#Se crea una lista para llenar
lista = llenarLista()

#Ahora se pide los dos elementos
numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

#Se entrega la funcion
posicion = obtenerPosicion(lista, numero)
print(f"El elemento esta en la posicion{posicion}")
posicion2 = obtenerPosicion(lista, numero2)
print(f"El elemento esta en la posicion2{posicion2}")


