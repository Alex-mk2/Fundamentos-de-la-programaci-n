



#Funciones para la lectura de archivos (Aqui sin dudas es necesario las funciones)
#Recordemos: una funcion es para realizar una operacion
#Ademas: Las funciones como tal contienen parametros o argumentos que permiten procesar los datos


#Ahora
#Funcion que permite la lectura de un archivo
#Dom: archivo
#Rec: lista con el contenido del archivo


#Modos de lectura
#Modo de lectura: "r"----> leer en modo lectura
#Modo de lectura: "w"----> Escribir un archivo




def leerArchivo(archivo):
    lista = [] #lista[0], lista[1].... lista[n]
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos: 
        informacion = datos.read()
        print("Primera vista de la lectura del archivo")
        informacion = informacion.splitlines() #Se divide el contenido en lineas
        for dato in informacion:
            auxiliar = dato.replace(",", "") #Reemplazamos las comas del archivo txt
            lista.append(auxiliar) #Limpiar el contenido, es decir, removiendo todo lo que no sirva...
        #Se cierra el archivo    
        datos.close() #Importante: siempre cerrar el archivo!
    return lista

#Se retorna la lista con elementos dentro del archivo

#Proceso de un archivo
lectura = leerArchivo("holaSoyArchivoAleer.txt")
print(lectura)