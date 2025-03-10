
#Se tiene lo siguiente para la funcion de lectura que debe considerar lo siguiente
#Tipos de dato: int, string, booleano



#Funcion que permite la lectura del archivo
#Dom: archivo
#Rec: lista con el contenido procesado

def leerArchivo(archivo):
    lista = [] #lista[0], lista[1].... lista[n]
    #Se abre el archivo en modo de lectura 
    with open(archivo, "r") as datos:
        next(datos)
        informacion = datos.read()
        print("Primera vista de la lectura del archivo")
        informacion = informacion.splitlines() #Se divide el contenido en lineas
        for dato in informacion:
            auxiliar = dato.strip().split(",")
            auxiliar[6] = float(auxiliar[6])
            auxiliar[7] = float(auxiliar[7])
            #Procesamiento fechas
            auxiliar[10] = int(auxiliar[10])
            lista.append(auxiliar) #Se manda a la lista el contenido
        #Se cierra el archivo    
        datos.close() 
    return lista


#Funcion que permite la busqueda por código
#Dom: lista X codigo
#Rec: El contenido asociado a ese código

def buscar_por_codigo(lista, codigo):
    personas = []
    buscar = 0
    for linea in lista:
        if(linea[0] == codigo):
            buscar = linea
            personas.append(buscar)
    
    return personas

#Buscar por estado
#Dom: lista, codigo
#Rec: personas

def buscar_activo(lista, activo):
    personas = []
    buscar = True
    for linea in lista:
        if(linea[3] == activo):
            buscar = linea
            personas.append(buscar)
    return personas


#Procesamiento del programa
lectura = leerArchivo("data.csv")

codigo = input("Ingrese un codigo: ").upper()

personas = buscar_activo(lectura, codigo)

print(personas)