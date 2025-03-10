


#Operacion para llenar elementos a una lista
lista = []
while(len(lista) < 10):
    numero = int(input("Ingrese un numero a la lista: "))
    lista.append(numero)

#Fin operacion para llenar elementos


#Para ordenar una lista como tal
i = 0


#Ciclo para ordenar una lista (uso de doble while)
while(i < len(lista) - 1):
    j = 0
    while(j < len(lista) - 1 - i):
        if(lista[j] > lista[j + 1]):
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp
        j = j + 1
    i = i + 1

#Verificaciones para indicar el orden de esta lista (descendente a ascendente o menor a mayor)...
print(f"La lista ordenada de menor a mayor es {lista}")


