#ejercicio 2

# Definimos la lista de reproducción original
Lista_original = ["Canción A", "Canción B", "Canción C", "Canción D", "Canción E"]

# Mostrar la lista original
print("Lista de reproducción original:")
print(Lista_original)

# Inicializar la variable para controlar si se desea seguir rotando
rotar = "si"

while rotar == "si" or rotar == "Si":
    # Solicitar la dirección de rotación
    direccion = input("¿Rotar a la izquierda (i) o derecha (d)?: ").lower()

    # Solicitar las posiciones que se desea rotar
    posiciones = int(input("¿Cuántas posiciones desea rotar?: "))
    
    # Ajustar las posiciones si es mayor que el tamaño de la lista
    tamaño_lista = len(Lista_original)
    posiciones = posiciones % tamaño_lista  # Esto asegura que las rotaciones no excedan el tamaño de la lista
    #Inicializamos las posiciones
    posiciones = -1 # Se usa -1 para que la condicion se ejecute correctamente
    
    # Mientras las posiciones no sea validas
    while (posiciones < 0): #condicion de borde         
        #Solicitar las posiciones que va a rotar
        posiciones = int(input("¿Cuántas posiciones desea rotar? "))
    
    
    #Ver si las posiciones si es mayor que el largo de la lista   
    tamaño_lista = len(Lista_original)
    posiciones = posiciones %  tamaño_lista # Que no exceda al mayor del tamaño
    #Primera condición
    # Si la dirección es izquierda
    if(direccion == "i"):
        for i in range(posiciones):
            # Extraer el primer elemento
            primera_cancion = Lista_original[0]
            # Mover todas las canciones una posición hacia adelante
            for j in range(tamaño_lista - 1):
                Lista_original[j] = Lista_original[j + 1]
            # Colocar la primera canción al final
            Lista_original[-1] = primera_cancion
    
    # Si la dirección es derecha
    elif(direccion == "d"):
        for i in range(posiciones):
            # Extraer el último elemento
            ultima_cancion = Lista_original[-1]
            # Mover todas las canciones una posición hacia atrás
            for j in range(tamaño_lista - 1, 0, -1):
                Lista_original[j] = Lista_original[j - 1]
            # Colocar la última canción al principio
            Lista_original[0] = ultima_cancion

    # Mostrar la lista rotada
    print("Lista de reproducción rotada:")
    print(Lista_original)