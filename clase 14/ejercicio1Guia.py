#Introduccion de nombres y apellidos para contar caracteres, nombre al reves, apellido por alfabeto

#Variables globales
VOCALES = "aeiou"
CONSONANTES = "qwrtypsdfghjklzxcvbnm"


#Se requieren tres funciones
#-*Contar caracteres (Listo)
#-*Nombre al reves (Listo)
#-*Apellido por alfabeto

#***************************Implementacion de funciones************************************#

#Funcion para contar los caracteres del nombre
#Dom: nombre 
#Rec: contador

def contarCaracteres(nombre):
    #Se definen un contador
    contador = 0
    for linea in nombre:
        for letra in linea:
            if(letra in VOCALES or letra in CONSONANTES):
                contador = contador + 1
    return (contador)


#Funcion para mostrar el nombre al reves
#Dom: nombre
#Rec: nombre (invertido)

def invertirNombre(nombre):
    reves = []
    i = len(nombre) - 1
    while(i >= 0):
        reves.append(nombre[i])
        i = i - 1
    return ''.join(reves)

#Segunda opcion de invertir un nombre
#Dom: Nombre
#Rec: Nombre invertido

def invertirNombrev2(nombre):
    reves = nombre[::-1]
    return reves


#Funcion para ordenar el apellido de forma alfabetica
#Dom: Apellido
#Rec: Apellido (ordenado alfabeticamente)

def ordenarAlfabetica(apellido):
    return ''.join(sorted(apellido))

#Ejecucion del programa

nombre = str(input("Ingrese un nombre: "))
apellido = str(input("Ingrese un apellido: "))
contarApellido = contarCaracteres(apellido)
contarNombre = contarCaracteres(nombre)
reves = invertirNombre(nombre)
revesv2 = invertirNombrev2(nombre)
ordenarApellido = ordenarAlfabetica(apellido)


#*************************Impresiones por pantalla*************************************
print(f"La cantidad de caracteres son {contarNombre}")
print(f"La cantidad de caracteres son {contarApellido}")
print(f"El nombre invertido es {reves}")
print(f"El apellido ordenado es {ordenarApellido}")
