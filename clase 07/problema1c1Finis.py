#Problema para calcular costos totales respecto a kilometros



#Se tiene en este caso solicitar al usuario que ingrese una cantidad de kilometros a recorrer

kilometros = int(input("Ingrese los kilometros a recorrer: "))

#Se tiene la tarifa inicial del viaje
tarifa_inicial = 4.00

#Se crea una variable para costos
costos = tarifa_inicial #4.00

#Se crea una variable para kilometro recorrido
kilometro_recorrido = 1.50

#Se crea un iterador
i = 1

#Mientras no alcance los kilometros recorridos
while(i <= kilometros):
    #Si es menor a 10 kilometros
    if(i <= 10):
        costos+= kilometro_recorrido
    else: #mayor a 10
        costos+= kilometro_recorrido - 0.30 
    i = i + 1

print(f"El costo total en {kilometros} kilometros recorridos es:", costos)

#Primeros datos

#Traza del programa
#costos = 4.00
#i = 1
#kilometros = 12

#Primer ciclo
#i = 2
#costos = 4.00 + 1.50 = 5.50

#Segundo ciclo
#costos = 5.50 + 1.50 = 7.00
#i = 3

#Tercer ciclo
#costos = 7.00 + 1.50 = 8.50
#i = 4

#Cuarto ciclo
#costos = 8.50 + 1.50 = 10.00
#i = 5

#Quinto ciclo
#costos = 10.00 + 1.50 = 11.50
#i = 6

#Sexto ciclo
#costos = 11.50 + 1.50 = 13.00
#i = 7

#Septimo ciclo 
#costos = 13.00 + 1.50 = 14.50
#i = 8

#Octavo ciclo 
#costos = 14.50 + 1.50 = 16.00
#i = 9

#Noveno ciclo
#costos = 16.00 + 1.50 = 17.50
#i = 10

#Decimo ciclo
#costos = 17.50 + 1.20 + 1.20 + 1.20 = 18.70 + 1.20 = 19.90 + 1.20 = 21.2
#i = 11

#






