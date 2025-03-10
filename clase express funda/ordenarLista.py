


#Operacion para llenar elementos a una lista
lista = []
while(len(lista) < 10):
    numero = int(input("Ingrese un numero a la lista: "))
    lista.append(numero)

#Fin operacion para llenar elementos


#Para ordenar una lista como tal
i = 0


#Ciclo para ordenar una lista (uso de doble while)
#Manera de ordenar se conoce como ordenamiento burbuja...
#dos ciclos while anidados------> complejidad n**2

#Ordenamiento por pivote--------> Divide y conquista (/2)

#pivote = (pequeño + largo) / 2

#Microservicios-monolitico-servicios...

#Las que se usan son monolitico-microservicios

#La importancia de base de datos-backend-front


while(i < len(lista) - 1): #i = 1
    j = 0
    while(j < len(lista) - 1 - i): #9----> 7
        if(lista[j] > lista[j + 1]): #lista[0] = 65 #lista[1] = 52
            temp = lista[j] #temp = 65
            lista[j] = lista[j + 1] #lista[0] = 52 
            lista[j + 1] = temp #65
        j = j + 1
    i = i + 1



#Traza del programa
#65 primer numero
#52 segundo numero




#Verificaciones para indicar el orden de esta lista (descendente a ascendente o menor a mayor)...
print(f"La lista ordenada de menor a mayor es {lista}")


