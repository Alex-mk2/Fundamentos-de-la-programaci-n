


#Estructura para construir funciones

#Dominio: Que es lo que recibe la funcion, en este caso es un (numero)
#Recorrido: Booleano, es decir, 0 o 1 para este caso
#Descripción: Esta funcion verifica si se ha ingresado un 1 o 0


def verificarUnoYCero(numero):
    if(numero == 0):
        return 0
    else:
        return 1
    

#Bloque principal

numero = int(input("Ingrese un 0 o 1: "))

#Se llama a la funcion para que realize la operacion

operacion = verificarUnoYCero(numero)

print("La operacion que se muestra por pantalla es: ", operacion)