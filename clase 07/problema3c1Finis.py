
#Problema 3 control c1 finis

#Ingresar elementos a una lista dinamica, en este caso es para el problema de consumo electrico

#Para agregar elementos de forma dinamica a la lista

#Se crea una condicion de borde
condicion = '0'

#Se crea una lista vacia
llenarLista = []

#Se crea un contador
contador = 0

#Se crea una suma
sumar_kilowatios = 0

#Se crea un iterador
i = 0

#Se crea una variable para obtener el mayor
mayor = 0

#Variable para obtener el menor 
menor = 0

#Variable para encontrar el promedio
promedio = 0

#Mientras que la condicion sea igual a '0' (string)
while(condicion == '0'): 
    numero = int(input("Ingrese el consumo electrico por dia: "))
    llenarLista.append(numero) 
    pregunta = (input("¿Desea agregar otro consumo por dia? (0/si /1/no): ")).strip().lower()
    
    #Se realiza la siguiente condicion
    if(pregunta in ['0', 'si']):
        condicion = '0'
    elif(pregunta in ['1', 'no']):
        condicion = '1'
    sumar_kilowatios+= llenarLista[contador] #Suma de los kWh 
    contador = contador + 1 #Contar los dias
    

#Se genera la condicion de lista dinamica, en este caso para el consumo electrico de luz


#Se trabajara con la lista que fue llenada

#Se crea tres iteradores
i = 0
j = 0
z = 0


#Se obtiene el primer elemento de la lista
mayor = llenarLista[0]
menor = llenarLista[0]


#Ciclo para encontrar el mayor de los elementos
while(i < len(llenarLista)):
    if(llenarLista[i] > mayor):
        #Se obtiene el mayor de los elementos
        mayor = llenarLista[i]
    i = i + 1

#Ciclo para encontrar el menor de los elementos
while(j < len(llenarLista)):
    if(llenarLista[j] < menor):
        menor = llenarLista[j]
    j = j + 1


#Ciclo para realizar el promedio de consumo de luz (recordar que no estan anidados)

#Calcular el largo de la lista
largoLista = len(llenarLista) #total de elementos

#Se recorre hasta el largo de la lista
while(z < len(llenarLista)):
    promedio+= (llenarLista[z])/largoLista
    z = z + 1



print("|------------------------Informe consumo electrico---------------------------------|")

print("Cantidad de dias de consumo: ", llenarLista)
print("Dias de consumo: ", contador)
print("Total consumido en kWh: ", sumar_kilowatios)
print("El mayor dia de consumo en kWh es: ", mayor)
print("El menor dia de consumo en kWh es: ", menor)
print("El promedio consumido en kWh es: ", promedio)