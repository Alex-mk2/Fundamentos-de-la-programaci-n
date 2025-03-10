#Ejercicio n°3
#Implementar un programa que lea el archivo MejoresSpotify2024.csv y haga lo siguiente:
#1.	Guardar en archivo top10.csv las 10 canciones con mejor ranking.
#2.	Mostrar canciones que comienzan con un caracter indicado por el usuario.
#3.	Mostrar canciones lanzadas durante un año indicado por el usuario.
#4.	Mostrar las 10 canciones de mayor duración (La duración debe ser mostrada en minutos).
#5.	Mostrar todas las canciones de un álbum indicado por el usuario


#Funcion que permite la lectura del archivo
#Dom: archivo
#Rec: una lista con el contenido leido

import csv
def leerArchivo(archivo):
    lista = []  # lista[0], lista[1].... lista[n]
    with open(archivo, "r", encoding="utf-8") as datos:
        next(datos)  # Omitir la primera cabecera
        informacion = datos.read()
        print("Primera vista de la lectura del archivo")
        informacion = informacion.splitlines()  # Dividir el contenido en líneas
        for dato in informacion:
            auxiliar = dato.strip().split(",")
            if len(auxiliar) == 7: #auxiliar = cabecillas del archivo
                auxiliar[0] = int(auxiliar[0].strip())  # Ranking
                auxiliar[1] = str(auxiliar[1]).strip()  # Título de la canción
                auxiliar[2] = str(auxiliar[2]).strip()  # Álbum
                auxiliar[3] = str(auxiliar[3]).strip()  # Artista
                auxiliar[4] = str(auxiliar[4]).strip()  # Fecha de lanzamiento
                auxiliar[5] = int(auxiliar[5].strip())  # Popularidad
                auxiliar[6] = int(auxiliar[6].strip())  # Duración
                lista.append(auxiliar)        
    return lista
                
                
#Funcion que me permite obtener las 10 canciones con mejor ranking
#Dom: lista con el contenido procesado
#Rec: top 10 canciones

def top10Canciones(lista):
    top10 = [] #lista vacía para almacenar las 10 canciones con mejor ranking
    #Ahora debemos ordenar la lista de canciones
    # Repetir 10 veces para obtener las 10 mejores canciones
    # # Usamos `_` porque no necesitamos el valor del contador en sí; solo queremos repetir el proceso 10 veces.
    #Además es útil para en este caso ya que solo importa que el codigo se repita 10 veces. 
    for _ in range(10): 
        mejor_ranking = 101  # Inicia con un valor alto de referencia, asumiendo que los rankings son menores a 100
        mejor_cancion = -1 #Se inicia con un valor minimo de referencia
        for cancion in lista:
            if cancion[0] < mejor_ranking: #Se compara si el ranking de la cancion actual es menor que el valor actual de mejor_rankinf
                if cancion not in top10:  # Verificamos que no esté en el top10
                    mejor_ranking = cancion[0] #Se actualiza y se guarda mejorranking
                    mejor_cancion = cancion #Se actualiza y se guarda la mejorcancion
        top10.append(mejor_cancion) # Se añade la cancion al top10
    return top10

#Primero necesitamos solicitar al usuario, que ingrese un carácter, con el que se va a buscar cada canción
caracter = input("Ingrese el carácter con el que comienzan las canciones: ").lower()

#Función que permite mostrar las canciones que comienzan con un carácter indicado por el usuario
#Dom: Lista con el contenido procesado
#Rec: Canciones que comienzan con el carácter indicado

def cancionesPorCaracter(lista, caracter):
    canciones = [] #Lista vacia para almacenae las canciones
    
    #Se recorre cada cancion en la lista
    for cancion in lista:
        titulo = cancion[1] #Obtenemos el título de la canción de cada elemento: [1] = nombre de la cancion
        #Si el primer carácter del título coincide con el carácter ingresado
        if(titulo[0].lower() == caracter): #Usamos .lower() pra ignorar mayúsculas/minúsculas
            canciones.append(cancion) #Agregar la canción a la lista ya que se encontro 
    return canciones




#Funcion que permite la escritura del archivo
#Dom: top10canciones 
#Rec: void
#Se usa encoding para que tome todos los caracteres especificos como tildes, simbolos etc

def escribirArchivo(archivo, top10, canciones):
    with open(archivo, "w", encoding="utf-8") as resultado:
        #Escribir las 10 canciones
        resultado.write(f"Las 10 mejores canciones son {top10}\n")           
        # Escribir las canciones que comienzan con el carácter indicado
        resultado.write(f"Canciones que comienzan con el carácter indicado {canciones}:\n")
        



#Procesamiento del programa
lectura = leerArchivo("MejoresSpotify2024.csv")
top10 = top10Canciones(lectura)
cancionesPorCaracter = cancionesPorCaracter(lectura, caracter)

#Escribir los resultados en un archivo
escribirArchivo("resultadostop10.csv", top10, cancionesPorCaracter) 

