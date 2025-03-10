#Construya un programa en python que permita calcular la raiz digital

#Raiz digital: sumar todos los digitos del numero que se ingresa

#Ejemplo = 12345-----> 1 + 2 + 3+ 4+5 = 15 ----> si la cadena es muy larga se debe volver a sumar 1 + 5 = 6
#Raiz digital de 12345 = 6

# Inicio del programa

# Pedir al usuario que ingrese un número
numero = input("Ingrese un número: ")

# Se crea una bandera
valido = True #bandera te verifica si algo se esta realizando correctamente o ser de verificaciones

# Se crea un iterador
i = 0

#Si esta dicho elemento o no se encuentra

#laboratorio

#Lista[i].... = lista[0]...lista[1]...lista[2]...lista[n]...


#Traza del programa
#i = 0, 1
#valido = True
#numero = 5, 4
#numero[i] = numero[0] = 5   ------> 5 se encuentra en '0123456789'------> f * (v) = f
#            numero[1] = 4   ------> falsa
#Mientras que iterador sea menor a la longitud del número
while i < len(numero): #len (para obtener el tamaño de la lista), # 0 < 5, # 1 < 5
    # Si el carácter en la posición i no es un dígito
    if numero[i] not in "0123456789": #No se encuentra en "0123456789", #falsa
        #Se cambia el estado de valido a falso
        valido = False
        break
    # Incrementa el iterador
    i += 1

if valido:  # Si es valido (verdadero)
    numero = int(numero)  # Se convierte a entero
    while numero >= 10:  # mientras el número sea mayor o igual a 10
        suma_digitos = 0  # Se crea una nueva variable
        temporal = numero  # Se guarda temporalmente #numero = 5, #temporal = 5
        while temporal > 0:  # Mientras el número temporal sea mayor a 0
            suma_digitos += temporal % 10  # Sumamos todos los dígitos divididos por el modulo de 10 (5 % 10)
            temporal //= 10  # Se hacen divisiones a todos los números en la variable temporal
        numero = suma_digitos  # Ahora el número tiene las operaciones realizadas
    print("La raíz digital es:", numero)
else:
    print("Número inválido")
