
#Ejercicio n°6

#Contruir un programa en python que indique si un numero es primo o no


#Inicio del programa

primo = int(input("Ingrese un numero: "))

#Se crea un contador

contador = 0

#Se crea un iterador
i = 1
#Aqui se crea la logica del programa


#En caso de que se quiera ingresar numeros negativos

if(primo <= 0):
    print("Error al ingresar numero")

#Se recorre con un ciclo while, mientras sea menor al numero ingresado

while(i <= primo):   
    
    if(primo % i == 0):

        #Sumamos al contador
        contador = contador + 1

    #Incrementamos el iterador
    i = i + 1


#Traza del código

#primo = 3,                        3 % 1 == 0 (verdadero)
#i = 1, 2, 3, 4                    3 % 2 == 0 (Falso)
#Contador = 0, 1, 2                3 % 3 == 0 (verdadero)

#Verificaciones, un numero primo solo tiene 2 divisores, 1 y por si mismo

if(contador == 2):
    print(primo, "Es numero primo")

else:
    print(primo, "No es un numero primo")





