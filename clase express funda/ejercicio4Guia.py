#Obtener raiz cubica en 5 elementos ingresados


#Para este problema en particular se requieren dos funciones 
#*-Funcion para llenar una lista
#*-Funcion para obtener la raiz cubica a cada uno de esos elementos

#***************************Implementacion de funciones************************************#


#Funcion que permite el llenado de la lista
#Dom: lista vacia
#Rec: lista con elementos

def llenarLista():
    lista_aux = []
    while(len(lista_aux) < 5):
        numero = int(input("Ingrese un numero a la lista: "))
        lista_aux.append(numero)
    return lista_aux


#Funcion para calcular la raiz cubica a cada uno de los elementos de la lista
#Dom: lista
#Rec: lista aplicada con raiz cubica

def raizCubica(lista):
    lista_aux = []
    i = 0
    while(i < len(lista)):
        raizCubica = lista[i] ** (1/3)
        lista_aux.append(raizCubica)
        i = i + 1
    return lista_aux




#Ejecucion del programa

#Se crea una lista para llenar los elementos
lista = llenarLista()

numero = raizCubica(lista)
print(numero)