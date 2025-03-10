import math
import matplotlib.pyplot as plt

#Similar al ejercicio anterior, pero con la condicion de que se puede generar n distancias
#Ademas en este ejercicio se busca saber el par de puntos mas cercano


#Distancia = raiz((x2 - x1) ** 2 + (y2 - y1)**2) 

#Ingresar las coordenadas tanto para x como y
xi = float(input("Ingrese la coordenada x del incidente: "))
yi = float(input("Ingrese la coordenada y del incidente: "))

#Se define la busqueda a una distancia minima
min_distancia = float('inf') #para buscar una distancia minima 
#Que exista una distancia minima
#min_distancia = False o min_distancia = -1
#Se setea un numero para ubicar el movil
movil_cercano = -1 #No existe, False

#Se define un contador
contador = 1

#Se define una lista para almacenar las distancias
lista_distancias_mov = []

#Se genera un ciclo infinito, es decir, cuando se escriba la palabra alto el programa se detiene


#While True----------> esto siempre será verdadero ----> Siempre se va a ejecutar
#Es una mala practica
#opcion = 1, 0----->Barajar alternativas para el usuario-----> switch-----> condicionales if, elif, else

while True:

    xm = input(f"Ingrese la coordenada x del móvil {contador} (o 'alto' para terminar): ") # x = 1, x = 2----->
    #Se pide coordenadas de x del auto
    if xm.lower() == 'alto': #se indique por consola la palabra "alto"
        break
    ym = input(f"Ingrese la coordenada y del móvil {contador}: ")
    #Se pide coordenadas y del auto a mover
    
    xm = float(xm) #Convertir este numero a flotante
    ym = float(ym) #
    #Se almacenan ambas coordenadas, adicional se genera dinamicamente los valores
    distancia = math.sqrt((xi - xm) ** 2 + (yi - ym) ** 2) 
    #Se calcula la distancia
    if distancia < min_distancia: #     
        #Se busca la distancia minima
        min_distancia = distancia
        #Ordenamiento por sort
        movil_cercano = contador
        #Se iguala al valor del contador
    
    lista_distancias_mov.append((xm, ym))
    contador += 1

#Verificaciones finales 
if movil_cercano != -1:
    print(f"El móvil más cercano es el móvil {movil_cercano} con una distancia de {min_distancia:.2f}")
else:
    print("No se ingresaron móviles.")


#Graficos, esto no debes aprenderlo pero si es algo interesante para ver de mejor grado los ejercicios


# Graficar las posiciones usando matplotlib
fig, ax = plt.subplots()
ax.scatter(xi, yi, color='red', label='Incidente')
for idx, (xm, ym) in enumerate(lista_distancias_mov, start=1):
    ax.scatter(xm, ym, label=f'Móvil {idx}')
    ax.text(xm, ym, f'{idx}', fontsize=12)

if movil_cercano != -1:
    xm_cercano, ym_cercano = lista_distancias_mov[movil_cercano - 1]
    ax.plot([xi, xm_cercano], [yi, ym_cercano], color='blue', linestyle='--', label='Más cercano')

ax.set_xlabel('Coordenada X') #Label de coordenada x
ax.set_ylabel('Coordenada Y') #Label de coordenada y
ax.legend()
plt.title('Posiciones de Incidente y Móviles') #Titulo del grafico
plt.grid(True)
plt.show()
