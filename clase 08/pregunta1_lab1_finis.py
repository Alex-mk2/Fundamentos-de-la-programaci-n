#Compra facil, estructura de envio
#Gastar más para mejores tasas de envio

#Se introduce una variable adicional: peso productos

#Se busca que el usuario ingrese precio de productos


#Inicio del programa

producto = int(input("Ingrese el precio del producto: "))
peso = int(input("Ingrese el peso del producto: "))

#Aqui se tienen los ingresos por pantalla

#Se crea una variable 
envio = 0

#Primera condicion cuando producto es menor a 50
if(producto < 50): #producto = 10
    if(peso <= 5): #peso = 5 
        envio = 10
    else:
        envio = 10 + (peso - 5) * 2 #5k-----> 7kg

#Para el caso que el producto se encuentre entre 50 y menor que 100      (Rango de numeros: (50-100)  
elif(producto >= 50 and producto < 100): #(50-99) #producto = 65 #peso = 7
    if(peso <= 5):
        envio = 5
    else:
        envio = 5 + (peso - 5) * 1.50 #5 + (7 - 5) * 1.5 = 8

#Para el caso que el producto sea mayor o igual a 100
elif(producto >= 100): #110 >= 100 peso = 8
    if(peso <= 5): #5kg
        envio = 0
    else:
        envio = 5 + (peso - 5) * 1 #5 + (8 - 5) * 1 = 8

#Traza del programa

#Primera condicion
#producto = 10
#peso = 5kg
#envio = 10

#Segunda condicion
#producto = 65
#peso = 7
#envio = 8

#Tercera condicion
#producto = 110
#peso = 8kg
#envio = 8


#De los valores de producto y peso

#Se imprime por pantalla el producto y peso
print(f"El envio de acuerdo al precio del producto {producto} y peso {peso} es: ", envio)
