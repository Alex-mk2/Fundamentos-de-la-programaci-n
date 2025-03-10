#FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
#SECCIÓN DEL CURSO: L-33
#PROFESOR DE TEORÍA: JOSÉ GONZÁLEZ
#PROFESOR DE LABORATORIO: DANIEL CALDERÓN
#
#AUTOR 
#NOMBRE: BASTIÁN MAUREIRA
#RUN: 20.202.237-5
#CARRERA: INGENIERÍA CIVIL MECATRÓNICA
#
# Variables globales: Variables que no cambiarán con el tiempo
MINUSCULAS = "abcdefghijklmnñopqrstuvwxyz"
MAYUSCULAS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
NUMEROS = "0123456789"
# Fin variables globales



# PROCESAMIENTO
# Se crea una bandera para cortar el bucle
finalizar = True

# PROCESAMIENTO
while finalizar:
    # Se le pide al usuario que ingrese una contraseña
    contrasena = input("Ingrese una contraseña: ")
    
    # Si la contraseña es "terminar", el ciclo se detiene
    if contrasena.lower() == "terminar":
        print("Se termina ejecución del programa")
        finalizar = False
    else:
        #Se trabajará a punta de banderas (es mas comodo diria yo)
        minuscula = False
        mayuscula = False
        punto = False
        coma = False
        numero = False
        puntoAndComa = False

        # Ahora se recorre cada caracter de la contraseña para verificar las reglas
        for caracter in contrasena:
            if(caracter in MINUSCULAS):
                minuscula = True
            if(caracter in MAYUSCULAS):
                mayuscula = True
            if(caracter in NUMEROS):
                numero = True
            if(caracter == ","):
                coma = True
            if(caracter == ";"):
                puntoAndComa = True

        # Verificar si se cumplen todas las condiciones
        if(minuscula and mayuscula and numero and coma and puntoAndComa):
            print("Cumple con todos los requisitos")
        else:
            print("Al menos falta un elemento")