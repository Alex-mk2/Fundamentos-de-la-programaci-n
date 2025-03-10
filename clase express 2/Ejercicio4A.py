
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

#Funcion que permite la escritura del archivo
#Dom: menorLatitud X mayorLatitud
#Rec: void

def escribirArchivo(archivo, menorLatitud, mayorLatitud, promLatitudes):
    with open(archivo, "w") as resultado:
        resultado.write(f"La menor latitud y ciudad es {menorLatitud}\n")
        resultado.write(f"La mayor latitud y ciudad es {mayorLatitud}\n")
        resultado.write(f"El promedio de las latitudes son {promLatitudes}\n")
        print("Se ha escrito el resultado correctamente\n")



#Procesamiento del programa
lectura = leerArchivo("lugares.csv")
mayorLatitud = mayorLatitud(lectura)
menorLatitud = menorLatitud(lectura)
promLatitudes = promedioLatitudes(lectura)
escribirArchivo("latitudes.csv", menorLatitud, mayorLatitud, promLatitudes)
