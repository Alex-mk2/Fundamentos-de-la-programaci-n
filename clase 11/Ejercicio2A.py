#A traves de archivos construya en python un programa que permita obtener:
#-Promedio de notas del curso
#-Nota más alta del curso
#-Nota mas baja del curso


#Funcion para leer un archivo
#Dom: Archivo
#Rec: lista con los elementos importantes

def leerArchivo(archivo):
    lista = []
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos:
        informacion = datos.read()
        informacion = informacion.splitlines() #Se divide el contenido en lineas
        for dato in informacion:
            auxiliar = dato.split(",") #Separamos los elementos del archivo
            auxiliar[2] = float(auxiliar[2])
            lista.append(auxiliar)
        #Se cierra el archivo    
        datos.close()
    return lista


#Funcion que permita obtener el promedio de las notas
#Dom: lista con el contenido leido
#Rec: promedio de notas

def calcularPromedio(lista):
    contador = 0

    #Se crea una variable para sumar notas
    suma_notas = 0

    #Recorremos cada linea de la lista
    for linea in lista:
        suma_notas+= linea[2]
        contador+=1
    return (suma_notas / contador)


#menor = 101
#if(lista[0] < menor) --------> lista[0] = 5
   #menor = lista[0] #menor = 5
#Lógica del porque se escoge numeros grande

#mayor = -1
#if(lista[0] > mayor) --------> lista[0] = 5
   #mayor = lista[0] #mayor = 5
#Lógica del porque se escoge numeros pequeños



#Funcion que calcula la mejor nota
#Dom: lista
#Rec: variable y alumno

def mayorNota(lista):
    mayor = -1
    alumno = 0
    for linea in lista:
        if(linea[2] > mayor):
            mayor = linea[2]
            alumno = linea[0]
    return (alumno, mayor)

#Funcion que entrega la menor nota dentro de un conjunto de datos
#Dom: lista
#Rec: variable y alumno con la menor nota

def menorNota(lista):
    menor = 101
    alumno = 0
    for linea in lista:
        if(linea[2] < menor):
            menor = linea[2]
            alumno = linea[0]
    return(alumno, menor)


#Funcion para la escritura del resultado
#Dom: archivo X promedio X mejorNota X menorNota
#Rec: void

def escribirArchivo(archivo, promedio, mejorNota, menorNota):
    with open(archivo, "w") as resultado:
        resultado.write(f"El promedio general del curso es {promedio}\n")
        resultado.write(f"La mejor nota es {mejorNota}\n")
        resultado.write(f"La nota mas baja es {menorNota}\n")
        print("Se ha escrito el resultado correctamente\n")


#Procesamiento de datos
lectura = leerArchivo("notas.txt")
promedio = calcularPromedio(lectura)
mejorNota = mayorNota(lectura)
menorNota = menorNota(lectura)
escribirArchivo("out.txt", promedio, mejorNota, menorNota)