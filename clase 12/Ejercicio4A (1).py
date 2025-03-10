
#Ejercicio 2 archivos
#Se tienen las siguientes ciudades en formato csv 
#Por lo cual se pide lo siguiente
#Obtener la mayor latitud de todas las ciudades en el csv y la ciudad correspondiente
#Obtener la menor latidud de todas las ciudades en el csv y la ciudad correspondiente
#Obtener el promedio de todas las latitudes en el csv
#Obtener el promedio de todas las logitudes en el csv #Pendiente
#Obtener la menor longitud en el csv, incluido su id, lugar #Pendiente
#Obtener la mayor longitud en el csv, incluido su id, lugar #Pendiente


#Funcion que permite la lectura del archivo
#Dom: archivo
#Rec: una lista con el contenido leido

def leerArchivo(archivo):
    lista = [] #lista[0], lista[1].... lista[n]
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos:
        next(datos) 
        informacion = datos.read()
        informacion = informacion.splitlines() #Se divide el contenido en lineas
        for dato in informacion:
            auxiliar = dato.strip().split(";")
            auxiliar[0] = int(auxiliar[0])
            auxiliar[2] = float(auxiliar[2])
            auxiliar[3] = float(auxiliar[3])
            lista.append(auxiliar) #Limpiar el contenido, es decir, removiendo todo lo que no sirva...
        #Se cierra el archivo    
        datos.close() #Importante: siempre cerrar el archivo!
    return lista


#Funcion que permite obtener la mayor latitud dentro del csv
#Dom: lista con el contenido
#Rec: latitudCiudad X mayor

def mayorLatitud(lista):
    mayor = -1
    latitudCiudad = 0
    for linea in lista:
        if(linea[2] > mayor):
            mayor = linea[2]
            latitudCiudad = linea[1]
    return (latitudCiudad, mayor)

#Funcion para obtener la menor latitud
#Dom: lista
#Rec: latitudCiudad X menor

def menorLatitud(lista):
    menor = 101
    latitudCiudad = 0
    for linea in lista:
        if(linea[2] < menor):
            menor = linea[2]
            latitudCiudad = linea[1]
    return (latitudCiudad, menor)


#Funcion para calcular el promedio de las latitudes
#Dom: lista
#Rec: promedio

def promedioLatitudes(lista):
    contador = 0
    suma_latitudes = 0
    for linea in lista:
        suma_latitudes += linea[2]
        contador+=1
    return (suma_latitudes / contador)


#Obtener el promedio de todas las logitudes en el csv #Pendiente
#Obtener la menor longitud en el csv, incluido su id, lugar #Pendiente
#Obtener la mayor longitud en el csv, incluido su id, lugar #Pendiente

#Función para calcular el promedio de longitudes
#Dom: Lista de contenido
#Rec: promedio de longitudes

def promedioLongitudes(lista):
    #Creamos un contador, para saber cuantas longitudes hemos sumado
    contador = 0 
    suma_longitudes = 0 #Se acumula la suma de longitudes
    for linea in lista:
        suma_longitudes = suma_longitudes + linea[3] # Se suma la longitud actual más la posición de la longitud
        contador = contador + 1 #Se incrementa el contador
    #Retorna el promedio de las longitudes
    return(suma_longitudes/contador)

#Función para calcular la menor longitud
#Dom: lista del contenido
#Rec: id; lugar y menor longitud

def menorLongitud(lista):
    menor = 101 #Se inicializa con un valor alto
    id = 0 #Se almacena el id de la ciudad
    lugar = "" #Se almacena el nombre del lugar con menor longitud
    for linea in lista:
        #Si la longitud actusl es menor que el valor almacenado
        if(linea[3] < menor):
            menor = linea[3] # Se guarda la menor latitud
            id = linea[0] # Se guarda el id 
            lugar = linea[1] #Se guarda el lugar
    #Retorna el id, lugar y menor longitud
    return(id, menor, lugar)         


#Función para obtener la mayor longitud
#Dom: lista del contenido
#Rec: id, lugar y menor longitud

def mayorLongitud(lista):
    mayor = -1 #Se inicializa con un valor menor 
    id = 0 #Se almacena el id de la ciudad
    lugar = "" #Se almacena el nombre del lugar con mayor longitud
    for linea in lista:
        #Si la longitud actual es mayor que el valor almacenado
        if(linea[3] > mayor):
            mayor = linea[3] #Se guarda la mayor longitud
            id = linea[0] #Se guarda el id
            lugar = linea[1] #Se guarda el lugar
    #Retorna el id, lugar y mayor longitud
    return(id, lugar, mayor)

#Funcion que permite la escritura del archivo
#Dom: menorLatitud, mayorLatitud, promLatitudes, promedioLongitudes, menorLongitud, MayorLongitud
#Rec: void

def escribirArchivo(archivo, menorLatitud, mayorLatitud, promLatitudes, promedioLongitudes, menorLongitud, mayorLongitud):
    with open(archivo, "w") as resultado:
        resultado.write(f"La menor latitud y ciudad es {menorLatitud}\n")
        resultado.write(f"La mayor latitud y ciudad es {mayorLatitud}\n")
        resultado.write(f"El promedio de las latitudes son {promLatitudes}\n")
        resultado.write(f"El promedio de las longitudes son {promedioLongitudes}\n")
        resultado.write(f"La menor longitud y ciudad es {menorLongitud}\n")
        resultado.write(f"La mayor longitud y ciudad es {mayorLongitud}\n")
        print("Se ha escrito el resultado correctamente\n")



#Procesamiento del programa
lectura = leerArchivo("lugares.csv")
mayorLatitud = mayorLatitud(lectura)
menorLatitud = menorLatitud(lectura)
promLatitudes = promedioLatitudes(lectura)
promedioLongitudes = promedioLongitudes(lectura) #obtener el promedio de las longitudes
menorLongitud = menorLongitud(lectura)#Obtener la menor longitud
mayorLongitud = mayorLongitud(lectura)#Obtener la mayor longitud
#Escribir los resultados en un archivo
escribirArchivo("latitudes.csv", menorLatitud, mayorLatitud, promLatitudes, promedioLongitudes, menorLongitud, mayorLongitud)

