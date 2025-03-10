
#A traves de un archivo, cree un programa que permita contar cuantas vocales hay dentro del archivo

#Archivos---------> implica leer algo-------->implica una funcion de lectura...


#Antes que todo variables globales
VOCALES = "aeiou"


#Primero, es necesario leer este archivo por lo cual necesitamos una funcion 
#Para archivos

#Descripcion: Funcion para la lectura de archivos
#Dom: Archivo
#Rec: lista con el contenido de un archivo

def leerArchivo(archivo):
    lista = []
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos:
        informacion = datos.read()
        informacion = informacion.splitlines() #Se divide el contenido en lineas
        for dato in informacion:
            auxiliar = dato.replace(",", "") #Reemplazamos las comas del archivo txt
            lista.append(auxiliar)
        #Se cierra el archivo    
        datos.close()
    return lista


#Se puede utilizar la funcion anterior para generar la lectura del archivo

#Ahora bien, hay que procesar esos datos ya que tenemos el contenido del archivo

#Funcion que procesara el contenido del archivo para contar vocales
#Dom: lista (contenido del archivo)
#Rec: contador (int) para saber cuantas vocales hay

#Nota: Al ser un archivo se debe recorrer a traves de for, ya que como tal estamos procesando
#El contenido de la lista (que en este caso es lo que obtuvimos del archivo)

def contarVocales(lista):
    contador = 0
    #Se recorre cada linea del archivo
    for linea in lista: #Nosotros vamos a recorrer cada parte del archivo o contenido que almacenamos en lista
        #Se recorre cada letra del archivo
        for letra in linea: #elemento del archivo letra[0], letra[1]...
            if(letra in VOCALES): 
                contador = contador + 1
    return contador


#Ahora que se tienen las vocales, tenemos que crear una funcion que permita la escritura de este resultado
#Ya que con archivos se debe estregar un txt 

#Funcion que permite la escritura de un resultado
#Dom: archivo X contador
#Rec: void (no retorna nada) #operacion...

def escribirArchivo(archivo, contador):
    with open(archivo, "w") as resultado:
        resultado.write(f"El archivo tiene {contador} vocales")
        print("Se ha escrito el resultado satisfactoriamente")


#Procesamiento de los datos
lectura = leerArchivo("vocales.txt")
totalVocales = contarVocales(lectura) #Ambos argumentos son iguales (lista = lista)
escribirArchivo("resultado.txt", totalVocales)

