# Solicitar la cantidad de jugadores
K = int(input("Ingrese la cantidad de participantes: "))

# Inicializar listas para almacenar los nombres y puntajes de los jugadores
nombres_jugadores = []
puntajes_jugadores = []

# Pedir el nombre de cada jugador y establecer su puntaje inicial a 0
contador = 0
#Mientras el contador sea menor que la cantidad de jugadores
while contador < K:
    # Se le solicita el nombre del jugador
    nombre = input("Ingrese el nombre del Jugador:")
    # Añadir el nombre a la lista de nombres
    nombres_jugadores.append(nombre)
    # Inicializar el puntaje del jugador a 0 y añadirlo a la lista de puntajes
    puntajes_jugadores.append(0)

    #Incrementamos el contador
    contador = contador + 1

# Realizamos las 3 rondas
ronda = 1
#Mientras haya rondas por jugar
while (ronda <= 3):
    print("Ronda:" , ronda)
    print("___")
    #Se inicializa la variable de contador para los puntajes de la ronda
    contador = 0

    while (contador < K):
        # Cada jugador lanza el dado
        puntaje = int(input("Puntaje " + nombres_jugadores[contador] +
" (1-6): "))
        # Sumar el puntaje al total acumulado del jugador
        puntajes_jugadores[contador] = puntajes_jugadores[contador] + puntaje
        contador = contador + 1
    #Se incrementa la rondas
    ronda = ronda + 1

# Calcular el puntaje máximo y mínimo
max_puntaje = puntajes_jugadores[0] # Inicializar el puntaje máximo
min_puntaje = puntajes_jugadores[0] # Inicializar el puntaje mínimo
jugador_max = nombres_jugadores[0]  # Inicializar el jugador con puntaje máximo
jugador_min = nombres_jugadores[0]  # Inicializar el jugador con puntaje mínimo

# Iniciar el contador para encontrar el máximo y mínimo
contador = 1
#
while (contador < K):
    # Verificar si el puntaje actual es mayor que el máximo
    if (puntajes_jugadores[contador] > max_puntaje): # Actualizar el máximo
        max_puntaje = puntajes_jugadores[contador] #Actualizar maximo puntaje
        jugador_max = nombres_jugadores[contador] # Actualizar el jugador máximo

    if (puntajes_jugadores[contador] < min_puntaje):
        min_puntaje = puntajes_jugadores[contador]
        jugador_min = nombres_jugadores[contador]
    #Se incrementa el contador
    contador = contador + 1

# Mostrar los resultados
print("Informe de Resultados")
print("___")
print("Puntaje Máximo: ", max_puntaje, "Jugador: ", jugador_max)
print("Puntaje Mínimo: ", min_puntaje, "Jugador: ", jugador_min)

# Ordenar y mostrar los puntajes de mayor a menor
i = 0
while(i < K):
    j = 0
    # Se Comparar puntajes hasta el penúltimo jugador
    while(j < K - 1):
        # Si el puntaje actual es menor que el siguiente, intercambia
        if (puntajes_jugadores[j] < puntajes_jugadores[j + 1]):
            # Intercambiar puntajes sin usar una variable temporal
            puntajes_jugadores[j], puntajes_jugadores[j + 1] = puntajes_jugadores[j + 1], puntajes_jugadores[j]
            # Intercambiar nombres sin usar una variable temporal
            nombres_jugadores[j], nombres_jugadores[j + 1] = nombres_jugadores[j + 1], nombres_jugadores[j]
        #Se incrementa el iterador
        j += 1
    #Se incrementa el iterador
    i = i + 1

# Mostrar puntajes ordenados
print("Listado Ordenado de Puntajes")
print("___")
contador = 0
while contador < K:
    print(nombres_jugadores[contador], ":", puntajes_jugadores[contador])
    contador = contador + 1