#Programa para realizar las funciones basicas a base de funciones


#Estructura inicial

#Funcion que permite el calculo de la suma a traves de dos elementos ingresados
#Dominio: numero X numero2
#Recorrido: numero

def calcularSuma(numero, numero2):
    numero3 = numero + numero2 
    return numero3 

#numero = 2
#numero2 = 3
#return = 5


#Funcion que permite el calculo de la multiplicacion a traves de dos elementos ingresados
#Dominio: numero X numero2
#Recorrido: numero

def calcularMultiplicacion(numero, numero2):
    numero3 = numero * numero2
    return numero3

#numero = 2
#numero = 3
#numero3 = 6

#Funcion que permite el calculo de la división a traves de dos elementos ingresados
#Dominio: numero X numero2
#Recorrido: numero

def calcularDivision(numero, numero2):
    numero3 = numero / numero2
    return numero3


#numero = 2
#numero2 = 3
#numero3 = decimal


#Funcion que permite el calculo de la resta a traves de dos elementos ingresados
#Dominio: numero X numero2
#Recorrido: numero

def calcularResta(numero, numero2):
    numero3 = numero - numero2
    return numero3

#numero = 2
#numero2 = 3
#numero3 = -1


#Main o menu principal, en donde se llaman a estas funciones

numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un segundo numero: "))

#Llamada a las funciones creadas
suma = calcularSuma(numero, numero2)
resta = calcularResta(numero, numero2)
multiplicacion = calcularMultiplicacion(numero, numero2)
division = calcularDivision(numero, numero2)


#Impresiones por pantalla de cada operacion
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicacion es: ", multiplicacion)
print("La division es: ", division)


#Como se puede notar, se disminuye mostrar codigo en el menu principal o main
#Al separar las operaciones en diferentes funciones
#Por lo cual le da más dinamismo al código y cohesion (cohesion es separar las cosas)
#Y no se sobrecarga el menu principal a base de escritura

