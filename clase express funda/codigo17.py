

#El problema visto anteriormente con estructura de while y condiccionales
#Pero ahora a modo de funciones, lo cual reduce mucho el problema en cuestion

#Misma libreria
from random import shuffle


#Descripcion: Funcion para saber si la lista se encuentra ordenada
#Dominio: lista, es lo que recibe la funcion
#Recorrido: booleano, recorrido es lo que entrega la funcion

def estaOrdenada(lista):
    #Se inicia un contador
    i = 0
    #Mientras no exceda el largo de la lista
    while (i < len(lista) - 1):
        #Si la lista es mayor a la posicion anterior
        if(lista[i] > lista[i+1]):
            #Retorna falso
            return False
        #Se incrementa el iterador
        i+=1
    #Se retorna verdadero cuando se encuentre ordenada
    return True

#Regla de oro: Usarlas solo para realizar una operacion

#Menu principal o llamado de funciones
entrada = input("Ingrese una lista de elementos: ")
#Hay que convertir a lista de string
lista = [int(x) for x in entrada.split(',')]
#Se agrega un contador para saber las veces que fue ordenada esta lista
contador = 0
#Se llama a la funcion para hacer el orden
listaOrdenada = estaOrdenada(lista)
#Mientras esta lista no se encuentre ordenada
while(not listaOrdenada):
    #Se desordena la lista
    shuffle(lista)
    #Se vuelve a desordenar la lista
    listaOrdenada = estaOrdenada(lista)
    #Se incrementa el contador
    contador+=1
print("Las veces que se tuvo que repetir para ordenar son", contador)