import random

#Se crean dos listas aleatorias
lista = list(range(0, random.randint(10, 100), random.randint(1,5)))
lista1 = list(range(0, random.randint(10, 100), random.randint(1,5)))
#random.shuffle(lista)
#Luego se revuelven estas listas


#Procesamiento del programa
lista_resultante = lista + lista1 #lista1[3] = [1, 2, 3, 4] #lista2[2] = [0,5,6]
#l_resultante = lista1 + lista2------> [1, 2, 3, 4, 0, 5, 6]
#Primera operacion hecha

#Se crea una nueva lista para almacenar los numeros
nueva_lista = []


#Procedimiento para quitar elementos repetidos
for elemento in lista_resultante: #por cada elemento en la lista_resultante
    if(elemento not in nueva_lista): #Si elemento no esta en nueva_lista
        nueva_lista.append(elemento) #nueva_lista.agregar(elemento)----->[1, 2, 3, 4, 0, 5, 6]------>
lista_resultante = nueva_lista

#lista_resultante = [x, y, z]-----> lista_resultante = nueva_lista------> nueva_lista = [1, 2, 3, 4, 5, 6]


#Procedimiento
#nueva_lista.agregar(elemento)----->[1, 2, 3, 4, 2, 5, 6]
#elemento[0]... elemento[1]...elemento[2]...elemento[n]----->pertenecen a lista_resultante
#nueva_lista[1, 2, 3, 4, 5, 6]

#Procedimiento 2 hecho


#Procedimiento para ordenar de mayor a menor
i = 0
listaOrdenadaDescendente = []
mayor = -1
while(lista_resultante): #hasta que esta lista quede vacia, seguimos buscando...
    mayor = max(lista_resultante) #Obtiene el maximo de cada elemento en la lista
    listaOrdenadaDescendente.append(mayor)
    lista_resultante.remove(mayor)

#listaOrdenadaDescendente = [6, 5, 4, 3, 2, 1]
#lista_resultante = []
#mayor = max(lista_resultante)

#Tercer procedimiento hecho

#Se imprime por pantalla el resultado de ambas listas
print(listaOrdenadaDescendente)
