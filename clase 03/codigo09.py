
#Construya un programa en python que permita ordenar por listas de numeros pares e impares


#Conceptos nuevos

#Lista: una lista permite almacenar elementos del tipo string, int, flotantes

#Operaciones: Se pueden realizar diferentes operaciones con las listas, ya siendo ordenarlas (sort)
#Recorrer las listas (por posiciones de los elementos)
#Trabajarlas como sublistas
#Divide y conquista
#Separar las listas
#Guardar elementos de las listas
#Y un monton de operaciones que pueden ser facilitadas por la libreria de str y otras librerias

#lower: convierte todas las palabras que se ingresen a minisculas "A"-----> "a"
#strip: devuelve una copia de la lista, sin espacios, sirve para eliminar espacios. "[A B C D]"----->[ABCD]

#Inicio del programa
 



#Para agregar elementos de forma dinamica a la lista

#Se crea una condicion de borde
condicion = '0'

#Se crea una lista vacia
llenarLista = []

#Se crea un contador
contador = 0

#Mientras que la condicion sea igual a '0' (string)
while(condicion == '0'): #True---->condicion = '0'
    numero = int(input("Ingrese un numero a la lista: ")) #numero = 1, #numero = 2
    llenarLista.append(numero) #el metodo append #llenarLista = [1, 2]
    pregunta = (input("Desea agregar otro numero (0/si /1/no): ")).strip().lower()
    
    #Se realiza la siguiente condicion
    if(pregunta in ['0', 'si']):
        condicion = '0'
    elif(pregunta in ['1', 'no']):
        condicion = '1'
    


#Se muestra por pantalla la lista llena de elementos
print("lista de elementos agregados: ", llenarLista)


#Ahora aqui se realiza la ejecucion del programa

#Se define un iterador
iterador = 0 #

#Se define una lista vacia para los pares
pares = []

#Se define una lista vacia para los impares
impares = []

#Mientras queden elementos en la lista



#Traza
#iterador = 0------->llenarLista = [1,2]-------> llenarLista[0] = 1, llenarLista[1] = 2 ----> 1 % 2 == 0
#           1------->llenarLista = [1,2]-------> llenarLista[1] = 2 -----> 2 % 2 == 0
#llenarLista = [1,2]
#pares = []
#impares = [1]

while(iterador < len(llenarLista)): #se paso del largo de la lista
    #Si el iterador de la lista (numero) se divide por el modulo de 2 igual a 0
    if(llenarLista[iterador] % 2 == 0): #iterador ----> llenarLista = [1, 2], iterador = 0, Falsa
        #Almacenamos los elementos pares a la lista de pares
        pares.append(llenarLista[iterador])
    #Caso que el elemento de la lista no sea un par
    else:
        impares.append(llenarLista[iterador]) #llenarLista[1]
    
    #Se incrementa el iterador
    iterador = iterador + 1


print("Los numeros pares son:", pares)

print("Los numeros impares son:", impares)
