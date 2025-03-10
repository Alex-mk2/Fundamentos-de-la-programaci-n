#Una fábrica de chocolates lo ha contratado para poder implementar un software que sea capaz de ingresar y analizar las cajas de un trasporte para calcular el costo de traslado. El sistema permite ingresar tres datos por cada caja: 
#Código del Tipo de Caja (1 = Pequeña, 2 = Mediana, 3 = Grande). 
#Peso de la caja en kilogramos.
#Frágil. (V=Verdadero, F=Falso) 

#Cantidad de cada uno de los tipos de cajas.
#Promedio del peso de cajas pequeñas, medianas y grandes.
#Promedio del peso de cajas frágiles y no frágiles.
#El mayor y menor peso entre todas las cajas (debe indicar si es pequeña, mediana o grande).
#Cantidad de cajas mayores a 100 kilogramos.
#Cantidad de cajas pequeñas que son frágiles y de menos de 1 kilogramo.
#Costo total por peso de cajas (1 kg cuesta 1000 pesos).

#Se crea iteradores
caja_pequeña = 0
caja_mediana = 0
caja_grande = 0
#Se cre iterador para el peso de cajas
peso_pequeñas = 0
peso_mediana = 0
peso_grandes = 0

# Se necesita acumular el promedio
promedioTotal = 0
promedioPorTipoCaja = 0
#Se crea una variable para contar cajas fragiles
cajas_pequeñas_fragiles = 0

#Se crea contadores por cada caja de acuerdo a si es fragil o no
contar_fragil = 0
contar_no_fragil = 0

#Mientras se cumpla esto 
while True:
    tipo_caja = int(input("Ingrese el tipo de caja (1 = Pequeña, 2 = Mediana, 3 = Grande)"))
    peso_caja = float(input("Ingrese el peso de la caja en kilogramos: "))
    fragil = input("¿Es frágil? (V/F): ")
    #Condicion de borde (en algun momento se debe detener el ciclo)
    if(tipo_caja == 0 or peso_caja == 0 or fragil == 0):
        break
    elif(tipo_caja == 1):
        #Se contabiliza que sea una caja pequeña
        caja_pequeña = caja_pequeña + 1
        peso_pequeñas = peso_caja
        #Si la caja es fragil
        if(fragil == 'V'):
            contar_fragil = contar_fragil + 1
        else:
            contar_no_fragil = contar_no_fragil + 1
        
    elif(tipo_caja == 2):
        #Se contabiliza que sea caja mediana
        caja_mediana = caja_mediana + 1
        peso_mediana = peso_caja
        if(fragil == 'V'):
            contar_fragil = contar_fragil + 1
        else:
            contar_no_fragil = contar_no_fragil + 1

    elif(tipo_caja == 3):
        #Se contabiliza que sea una caja grande
        caja_grande = caja_grande + 1
        peso_grandes = peso_caja
        if(fragil == 'V'):
            contar_fragil = contar_fragil + 1
        else:
            contar_no_fragil = contar_no_fragil + 1
    

#Para obtener el promedio de las cajas bastaria con obtener el peso de cada caja y luego dividirlo 
#Por el total de cada caja (pequeña, grande, mediana que se conto)
promedioTotal = (peso_pequeñas + peso_mediana + peso_grandes)/(caja_grande + caja_mediana + caja_pequeña)


#Para obtener el peso por cada tipo (fragil, no fragil) bastaria sumar todos los pesos de cajas y de acuerdo
#A si son fragiles o no, obtener el promedio
promedioPorTipoCaja = (peso_pequeñas + peso_mediana + peso_grandes)/(contar_fragil + contar_no_fragil)


#Si se imprime cada caja
print(f"La cantidad de cajas pequeñas son {caja_pequeña}")
print(f"La cantidad de cajas medianas son {caja_mediana}")
print(f"La cantidad de cajas grandes son {caja_grande}")
print(f"El promedio de las cajas son {promedioTotal}")
print(f"El promedio de acuerdo al tipo de caja son {promedioPorTipoCaja}")
#En este caso solo se esta contabilizando cada caja (sea grande, pequeña y mediana)
    
    
