#Problema 1

#Ingrese un numero inicio y un numero fin para obtener el rango de numeros primos

inicio = int(input("Ingrese el primer numero: "))
fin = int(input("Ingrese el segundo numero: "))



#Primero saber si el numero menor es mayor

if(inicio > fin):
    print("Error al ingresar los numeros, el primero debe ser menor")

#Caso contrario se recorre en un rango de numeros y se aplica la lógica para encontrar el número primo
else:
    for numero in range(inicio, fin + 1):
        contador = 0
        i = 1
        while(i <= numero):
            if(numero % i == 0):
                contador = contador + 1
            i = i + 1
        if(contador == 2):
            print(numero, "Es numero primo")


