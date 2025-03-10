
#Construya en python un programa que permita calcular la distancia entre dos puntos.
#Adicionalmente el programa debe indicar cual es el objetivo más cercano (se refiere a los puntos cartesianos)

#Distancia entre dos puntos = raiz((x2 - x1)°2 + (y2 - y1)°2)

#Primero debemos importar librerias, aqui se importa la libreria de matematicas sqrt (raiz cuadrada)
from math import sqrt


#Inicio del programa

print("Ingrese los valores de la coordenada x: ")
x1 = float(input())
y1 = float(input())

print("Ingrese los valores de la coordenada y: ")
x2 = float(input())
y2 = float(input())

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre los dos puntos son: ", distancia)

