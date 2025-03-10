#Problema de foto finish
#En general son calculos de distancia
#Para eso es necesario que se reciban dos listas con elementos

lista = list(map(int, input("Ingrese el primer avance: ").split('-'))) #...... 80706050
lista2 = list(map(int, input("Ingrese el segundo avance: ").split('-')))
distancia = int(input("Ingrese una distancia: "))

#Se crea un iterador
i = 0

#Se crean variables de operacion
distancia_acum1 = 0 #..... sumar cada elemento de la secuencia...
distancia_acum2 = 0
foto_j1 = 0
foto_j2 = 0 #turno 0.... d_acum = 40


#Mientras no alcance el largo de la distancia
while(distancia_acum1 < distancia and i < len(lista)):
    distancia_acum1 += lista[i] #Para sumar notas...
    foto_j1 += 1 #contador
    i = i + 1 #romper el ciclo

#oye hazme esto
j = 0

#Mientras no alcance el largo de la distancia y el largo de la lista
while(distancia_acum2 < distancia and j < len(lista2)):
    distancia_acum2 += lista2[j]
    foto_j2 += 1
    j = j + 1


#Para realizar las verificaciones entre ambos resultados
if(foto_j1 < foto_j2):
    print("Ganador jugador 1")
elif(foto_j2 < foto_j1):
    print("Ganador jugador 2")

else:
    print("Empate entre ambos")

