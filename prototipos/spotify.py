#Funcion de lectura de un archivo
#En general se requiere obtiener la lista de mejores artistas

#Librerias a usar (al menos para esta ocasión)
import csv

#Funciones requeridas
#Lectura de archivo
#Escritura
#Funcion para obtener los 10 mejores


#Funcion para leer un archivo
#Dom: Archivo
#Rec: lista con los elementos importantes

def leerArchivo(archivo):
    lista = []
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos:
        read_data = csv.reader(datos)
        next(read_data)
        for dato in read_data:
            dato[0] = int(dato[0])
            dato[5] = int(dato[5])
            dato[6] = int(dato[6])
            lista.append(dato)
        #Se cierra el archivo    
        datos.close()
    return lista

#Como esta data ya esta procesada, ahora necesitamos obtener los 10 mejores artistas

#Descripcion: Funcion para obtener los 10 mejores artistas
#Dom: lista procesada csv
#Rec: los 10 mejores artistas (popularidad)

def obtenerMejores(lista):
    mejores = []
    name = []
    for linea in lista:
        if(len(mejores) < 10):
            mejores.append(linea[5])
            if(len(name) < 10):
                name.append(linea[1])
    return (name, mejores)



#Funcion cardenas
def top10Canciones(lista):
    top10 = [] #lista vacía para almacenar las 10 canciones con mejor ranking
    #Ahora debemos ordenar la lista de canciones
    # Repetir 10 veces para obtener las 10 mejores canciones
    for _ in range(10):  # Queremos los 10 mejores
        mejor_ranking = 101  # Inicia con un valor alto de referencia
        mejor_cancion = -1
        for cancion in lista:
            if cancion[0] < mejor_ranking:
                if cancion not in top10:  # Verificamos que no esté en el top10
                    mejor_ranking = cancion[0]
                    mejor_cancion = cancion
        top10.append(mejor_cancion)
    return top10


#Procesamiento del programa
lectura = leerArchivo("MejoresSpotify2024.csv")
mejores = obtenerMejores(lectura)
print(mejores)