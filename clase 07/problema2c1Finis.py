
#Se tiene una lista de numeros enteros
#Se desea sumar tanto por numeros pares como numeros impares
#Ejercicio control 1 finis

#Adicional se entrega una lista con numeros pares e impares

lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]



#Ejecucion del programa

#Se crean dos listas vacias

pares = []
impares = []

suma_pares = 0
suma_impares = 0
contador_pares = 0
contador_impares = 0

#Se crea un iterador
i = 0
#Mientras no exceda la lista de lista_enteros

while(i < len(lista_enteros)):
    #Si se encuentra el numero par
    if(lista_enteros[i] % 2 == 0): #75 % 2 == 0
        pares.append(lista_enteros[i])
        suma_pares += lista_enteros[i]
        contador_pares = contador_pares + 1
        
    else:
        impares.append(lista_enteros[i])
        suma_impares+= lista_enteros[i]
        contador_impares = contador_impares + 1
    #Se incrementa contador
    i = i + 1



#Traza del programa
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75] = 11
#i = 0
#contador_p = 1
#contador_i = 0
#suma_p = 10
#suma_i = 0
#lista_pares = [10]
#lista_impares = []

#Segundo ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 1
#contador_p = 1
#contador_i = 1
#suma_p = 10
#suma_i = 23
#lista_pares = [10]
#lista_impares = [23]


#Tercer ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 2
#contador_p = 1
#contador_i = 2
#suma_p = 10
#suma_i = 23 + 45 = 68
#lista_pares = [10]
#lista_impares = [23, 45]

#Cuarto ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 3
#contador_p = 2
#contador_i = 2
#suma_p = 10 + 68 = 78
#suma_i = 23 + 45 = 68
#lista_pares = [10, 68]
#lista_impares = [23, 45]

#Quinto ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 4
#contador_p = 2
#contador_i = 3
#suma_p = 10 + 68 = 78
#suma_i = 23 + 45 + 91 = 159
#lista_pares = [10, 68]
#lista_impares = [23, 45, 91]

#Sexto ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 5
#contador_p = 3
#contador_i = 3
#suma_p = 10 + 68 + 24 = 102
#suma_i = 23 + 45 + 91 = 159
#lista_pares = [10, 68, 24]
#lista_impares = [23, 45, 91]


#Septimo ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 6
#contador_p = 3
#contador_i = 4
#suma_p = 10 + 68 + 24 = 102
#suma_i = 23 + 45 + 91 + 35 = 194
#lista_pares = [10, 68, 24]
#lista_impares = [23, 45, 91, 35]


#Octavo ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 7
#contador_p = 4
#contador_i = 4
#suma_p = 10 + 68 + 24 + 46 = 148
#suma_i = 23 + 45 + 91 + 35 = 194
#lista_pares = [10, 68, 24, 46]
#lista_impares = [23, 45, 91, 35]

#Noveno ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 8
#contador_p = 5
#contador_i = 4
#suma_p = 10 + 68 + 24 + 46 + 52 = 200
#suma_i = 23 + 45 + 91 + 35 = 194
#lista_pares = [10, 68, 24, 46, 52]
#lista_impares = [23, 45, 91, 35]

#Decimo ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 9
#contador_p = 5
#contador_i = 5
#suma_p = 10 + 68 + 24 + 46 + 52 = 200
#suma_i = 23 + 45 + 91 + 35 + 33 = 227
#lista_pares = [10, 68, 24, 46, 52]
#lista_impares = [23, 45, 91, 35, 33]

#Undecimo ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 10
#contador_p = 5
#contador_i = 6
#suma_p = 10 + 68 + 24 + 46 + 52 = 200
#suma_i = 23 + 45 + 91 + 35 + 33 + 75 = 302
#lista_pares = [10, 68, 24, 46, 52]
#lista_impares = [23, 45, 91, 35, 33, 75]

#Doceavo ciclo
#lista_enteros = [10, 23, 45, 68, 91, 24, 35, 46, 52, 33, 75]
#i = 11
#contador_p = 5
#contador_i = 6
#suma_p = 10 + 68 + 24 + 46 + 52 = 200
#suma_i = 23 + 45 + 91 + 35 + 33 + 75 = 302
#lista_pares = [10, 68, 24, 46, 52]
#lista_impares = [23, 45, 91, 35, 33, 75]
#Menu principal, se realiza el llamado al print

print("La lista de numeros pares son: ", pares)
print("La lista de numeros impares son: ", impares)
print("La suma de los numeros pares son: ", suma_pares)
print("La suma de los numeros impares son: ", suma_impares)
print("La cantidad de numeros pares son: ", contador_pares)
print("La cantidad de numeros impares son: ", contador_impares)