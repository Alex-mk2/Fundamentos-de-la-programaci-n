
#Ejercicio pokedex


#Funcion que permite la lectura del archivo
#Dom: archivo
#Rec: una lista con el contenido leido

def leerArchivo(archivo):
    lista = [] #lista[0], lista[1].... lista[n]
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos: 
        next(datos) #Sirve para omitir la primera cabecera 
        informacion = datos.read()
        print("Primera vista de la lectura del archivo")
        informacion = informacion.splitlines() #Se divide el contenido en lineas
        for dato in informacion:
            auxiliar = dato.strip().split(";")
            auxiliar[0] = int(auxiliar[0])
            auxiliar[4] = int(auxiliar[4])
            auxiliar[7] = float(auxiliar[7]) 
            auxiliar[8] = float(auxiliar[8]) 
            auxiliar[9] = int(auxiliar[9])   
            auxiliar[10] = int(auxiliar[10]) #ataque
            auxiliar[11] = int(auxiliar[11]) 
            auxiliar[12] = int(auxiliar[12]) 
            auxiliar[13] = int(auxiliar[13])
            lista.append(auxiliar) #Limpiar el contenido, es decir, removiendo todo lo que no sirva...
        #Se cierra el archivo    
        datos.close() #Importante: siempre cerrar el archivo!
    return lista


#Funcion que me permite obtener el mayor de los ataque de los pokemones
#Dom: lista con el contenido procesado
#Rec: elemento mayor

def mayorAtaque(lista):
    mayor = -1
    nombreP = 0
    for linea in lista:
        if(linea[10] > mayor):
            mayor = linea[10]
            nombreP = linea[1] #Lo que hace es identificar el nombre del pokemon con mayor ataque
    return(nombreP, mayor)


#Funcion que permite obtener el pokemon con el menor ataque
#Dom: lista con el contenido
#Rec: nombreP X menor

def menorAtaque(lista):
    menor = 101
    nombreP = 0
    for linea in lista:
        if(linea[10] < menor):
            menor = linea[10]
            nombreP = linea[1]
    return (nombreP, menor)


#Funcion que permite obtener el promedio de ataque de un pokemon
#Dom: lista
#Rec: promedio ataque pokemon

def prom_ataque(lista):
    suma = 0
    prom = 0
    for linea in lista:
        suma+= linea[10]
        prom = prom + 1
    return(suma/prom)


#Funcion que permite la escritura del archivo
#Dom: menorAtaque X mayorAtaque
#Rec: void

def escribirArchivo(archivo, menorAtaque, mayorAtaque, promAtaque):
    with open(archivo, "w") as resultado:
        resultado.write(f"El menor ataque es {menorAtaque}\n")
        resultado.write(f"El mayor ataque es {mayorAtaque}\n")
        resultado.write(f"El promedio del ataque es {promAtaque}")
        print("Se ha escrito el resultado correctamente\n")



#Procesamiento de los datos
lectura = leerArchivo("pokedex.csv")
menorAtaque = menorAtaque(lectura)
mayorAtaque = mayorAtaque(lectura)
promA = prom_ataque(lectura)
escribirArchivo("resultadoPokemones.csv", menorAtaque, mayorAtaque, promA)


#Ejercicios propuestos
#Diseñe la funcion que permita calcular el mayor peso de un pokemon con los datos escritos
#Diseñe la funcion que permita calcular el promedio de las velocidades de todos los pokemon
#Diseñe una funcion que permita calcular la mayor y menor defensa de un pokemon, y que tambien muestre todos los nombres del archivo
#(name, german_name, japanese_name)
#Diseñe la función que permita obtener el mayor y menor hp para un pokemon, incluido todos sus nombres

