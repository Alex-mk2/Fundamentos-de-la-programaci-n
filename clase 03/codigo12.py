#Ejercicio tipo pep usach 1-2018

#Pregunta para ordenar elementos

#Uno de los algoritmos de ordenamiento más extraños en el mundo de la 
#programación es el algoritmo conocido como random sort o 
#shotgun sort, el cuál funciona de la siguiente forma: 
#• Si la lista está ordenada, se entrega la lista. 
#• Si la lista no está ordenada, se revuelven aleatoriamente sus elementos y se revisa nuevamente.  
# Este algoritmo es altamente ineficiente, pero se desea conocer en la práctica cuán ineficiente 
# es y cómo varía en la medida que la lista a ordenar crece, por lo que se le solicita a usted
# que construya un programa que ingrese una lista, de números enteros positivos, 
# e indique cuántas veces debieron reordenarse los elementos para ordenarse de menor a mayor.
# Para su solución considere que:   
# Dentro del módulo random existe la función shuffle, que revuelve aleatoriamente
# los elementos de una lista. 
# La función no retorna la lista revuelta, sino que modifica internamente el orden de sus elementos. 
# •No  se  pueden  usar  métodos,  ni funciones  que  ordenen  para  el desarrollo  de  su solución



#Importacion de librerias
from random import shuffle #revolver los elementos de forma aleatoria

#Se le pide al usuario que ingrese una lista de elementos
lista = str(input("Ingrese una lista de elementos: ")) #1, 2, 3, 10, 15, 20

#Se define una lista vacia
listaOrdenada = []


#Se declara un iterador
iterador = 0

#Se crea un contador
contador = 0

#Se declara una bandera        #Una lista auxiliar
comilla = ""


#lista = [1,2,3,4,5,10] -------> [1234510]------> lista[0] = 1, lista[1] = 2, lista[2] = 3.... [,,,,,,]
#iterador = 0
#comilla = ['1234510']
#listaOrdenada = [1, 2, 3, 4, 5, 10]

#Mientras sea menor que la lista que se esta ingresando
while(iterador < len(lista)): #1 2 3 4 5
    #Si la entrada es distinta a ,
    if(lista[iterador] != ','):
        #Se guardan los elementos de la lista en comilla
        comilla +=lista[iterador] #
    else: #lista[iterador] == ','
        #Se guarda el elemento en la lista
        listaOrdenada.append(int(comilla))
        #Se reinicia la variable comilla
        comilla = "" #Vuelve a estar vacia

    #Se incrementa el iterador 
    iterador = iterador + 1
#Se añade el ultimo elemento
listaOrdenada.append(int(comilla)) #10

#Se crea una bandera
estaOrdenada = True #en el caso de que la lista se encuentre ordenada, se entrega la lista

#Se crea otro iterador (usualmente se utiliza j con matrices), recorrer una matriz es con [i][j]
#matriz[i][j] matriz[0][0], matriz[1][1]

j = 0

#Aqui se debe hacer el segundo ciclo
#Se ejecutara este while de forma independiente

#Mientras que j < largo(ListaOrdenada)
#listaOrdenada = [1,2,3,4,5,10]----->largoListaOrdenada = 5 - 1 = 4
#j = 0, 1
#listaOrdenada[0] = 1  -----------> 1 > 2   como j = 0 // listaOrdenada[j]------> listaOrdenada[0] = 1
#                                                    //  listaOrdenada[j + 1]----> listaOrdenada[0 + 1] = 2
# listaOrdenada[1] = 2

#Nueva tabla para iterador
#j = 1
#listaOrdenada[1] = 2
#listaOrdenada[1 + 1] = 3  ------> 2 > 3


while(j < len(listaOrdenada) - 1):
    #Si el elemento es mayor al siguiente elemento
    if(listaOrdenada[j] > listaOrdenada[j + 1]): 
        #Si el elemento de esta lista ordenada es mayor al elemento siguiente
        estaOrdenada = False
        #Se rompe el ciclo
        break;
    j = j + 1

#Luego se debe hacer otro ciclo mas para evaluar si no esta ordenada


#Si la lista no se encuentra ordenada, revuelve los elementos


#Cuenta cuantas veces se tuvo que ordenar la lista

while(not estaOrdenada): #estaOrdenada = True #not estaOrdenada = False
    #Se ordena la lista
    shuffle(listaOrdenada) #Ordena los numeros de forma aleatoria
    #Se incrementa el contador
    contador = contador + 1

    #Se verifica la bandera
    estaOrdenada = True

    #Se crea otro iterador
    k = 0
    #Se recorre nuevamente la lista
    while(k < len(listaOrdenada) - 1):
        #Si el elemento es mayor al siguiente elemento
        if(listaOrdenada[k] > listaOrdenada[k+1]):
            #Se setea la bandera a falso
            estaOrdenada = False
            break
        k = k + 1

print("Cantidad de veces que esta lista se ordeno es: ", contador)












