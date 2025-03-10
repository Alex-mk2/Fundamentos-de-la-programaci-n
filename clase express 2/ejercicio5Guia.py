#Finalmente tenemos los archivos
#En general los cambios que se deben hacer son minimos


#Funciones requeridas
#*-Lectura de archivo txt
#*-Escritura archivo txt
#*-Funcion elevado


#Funcion para la lectura de archivo
#Dom: Archivo
#Rec: lista con el contenido

def leerArchivo(archivo):
    lista = []
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos:
        informacion = datos.read()
        informacion = informacion.splitlines() #Se divide el contenido en lineas
        for dato in informacion:
            auxiliar = dato.strip().split(";")#Reemplazamos las comas del archivo txt
            lista.append(auxiliar)
        #Se cierra el archivo    
        datos.close()
    return lista #('2')


#Funcion que eleva al numero que se encuentra en el txt
#Dom: lista con el contenido
#Rec: numero elevado...

def elevarElemento(lista):
    elevado = []
    numero = int(lista[0][0])#'2'-------> 2 (int) #Solo se aplica cuando hay un elemento en el archivoS
    for potencia in range(1,10): #(9)
        resultado = numero ** potencia 
        elevado.append(resultado)
    return elevado


#Funcion para escribir un archivo
#Dom: archivo X elevado
#Rec: void

def escribirArchivo(archivo, elevado):
    with open(archivo, "w") as resultado:
        resultado.write(f"el numero elevado hasta 9 es {elevado}\n")



#Ejecucion principal
lectura = leerArchivo("ejercicio5.txt")
elevado = elevarElemento(lectura)
escribirArchivo("elevado.out", elevado)
