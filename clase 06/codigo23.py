#Diseñe un programa que permita ordenar temperaturas desde mayor a menor temperatura


#Definicion de funciones

#Se utilizara una funcion para ordenar las temperaturas de mayor a menor
#Se utilizara otra funcion para obtener las temperaturas
#Fin de definicion de funciones



#Definicion de constantes

#No hay

#Fin definicion de constantes


#Funcion a generar
#Descripcion: funcion que permita ordenar las temperaturas
#Dom: lista de temperaturas
#Rec: lista temperaturas ordenada

#Fin procedimiento funciones


#Construccion de la funcion

def ordenarTemperaturas(listaTemperaturas):
    #Se crea una lista vacia para ordenar las temperaturas
    listaOrdenada = []
    while(len(listaTemperaturas)!= 0): #Mientras sea distinto de 0
        print(listaTemperaturas) #Se imprime por primera vez las temperaturas
        mayor = listaTemperaturas[0] #Se toma el mayor de las temperaturas
        #Se crea un iterador
        i = 0
        while(i < len(listaTemperaturas)):
            #En caso de que sea menor que la lista de temperaturas
            if(mayor < listaTemperaturas[i]): #5.1 < 
                #Se toma el nuevo elemento
                mayor = listaTemperaturas[i] #20
            i = i + 1
        #Se agrega el elemento a la lista ordenada
        listaOrdenada.append(mayor)
        #Se elimina el elemento de la lista tem
        listaTemperaturas.remove(mayor)
    return listaOrdenada




#Traza de la funcion

#Primera iteracion
#listaTemperaturas = 5.1, 10.5, 20
#listaOrdenada = []
#i = 0
#mayor = listaTemperaturas[0] = 5.1


#Segunda iteracion
#listaTemperaturas = 5.1, 20
#listaOrdenada = [10.5]
#i = 1
#mayor = listaTemperaturas[0] = 5.1

#Tercera iteracion
#listaTemperaturas = 5.1
#listaOrdenada = [20, 10.5]
#i = 2
#mayor = listaTemperaturas[0] = 5.1

#Cuarta iteracion
#listaTemperaturas = ' '
#listaOrdenada = [20, 10.5, 5.1]
#i = 3
#mayor = listaTemperaturas[0] = 5.1

#Quinta iteracion
#listaTemperaturas = ' '
#listaOrdenada = [20, 10.5, 5.1]
#i = 3
#mayor = listaTemperaturas[0] = 5.1

#Descripcion: Funcion que permite obtener las temperaturas
#Dom: numero X listaOrdenada
#Rec: listaOrdenada




def obtenerTemperaturas(numero, listaOrdenada):
    listaTemperaturas = [] #Lista vacia para almacenar los elementos
    i = 0 #Se crea un iterador
    while(i < numero): #Mientras sea menor al numero
        listaTemperaturas.append(listaOrdenada[i]) #Guardamos las temperaturas ordenadas
        i = i + 1 #Se incrementa iterador
    return listaTemperaturas


#Segunda traza de funcion
#i = 0
#listaOrdenada = [20, 10.5, 5.1]
#listaTemperaturas = [20]
#numero = 2

#Segundo ciclo
#i = 1
#listaOrdenada = [20, 10.5, 5.1]
#listaTemperaturas = [20, 10.5]
#numero = 2

#Tercer ciclo
#i = 2
#listaOrdenada = [20, 10.5, 5.1]
#listaTemperaturas = [20, 10.5]
#numero = 2

#Menu principal, llamados de funciones y a usuario

temperaturas = input("Ingrese una lista de temperaturas: ").split()
numero = int(input("Ingrese un numero: "))

#Se realiza el llamado a la funcion
listaOrdenada = ordenarTemperaturas(temperaturas)

#Se obtienen las temperaturas ordenadas
listaTemperaturas = obtenerTemperaturas(numero, listaOrdenada)

print("Las temperaturas mas altas son: ", listaTemperaturas)






