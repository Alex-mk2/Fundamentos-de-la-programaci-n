

#Escribir programa que revisa dos fechas en formato DD/MM/YYYY
#Procedimiento completo en este caso se ingresan cada formato de fechas

fecha1 = input("Ingrese una fecha en formato (DD-MM-YYYY): ")
fecha2 = input("Ingrese una segunda fecha en formato (DD-MM-YYYY): ")

#Se procede a convertir estas fechas
listaFecha1 = fecha1.split("-") #13-10-1997--------> '13101997'
listaFecha2 = fecha2.split("-") #13-10-2024--------> '13102024'
#Fechas convertidas

#Se transforma cada variable
dia1 = int(listaFecha1[0]) #'13'-------->(13)
mes1 = int(listaFecha1[1]) #'10'-------->(10)
anio1 = int(listaFecha1[2])#'1997'------>(1997)


#Se transforma para la primera y segunda lista de fechas
dia2 = int(listaFecha2[0]) #'13'--------->(13)
mes2 = int(listaFecha2[1]) #'10'--------->(10)
anio2 = int(listaFecha2[2])#'2024'------->(2024)


#Unidades de medida deben ser las mismas para realizar operaciones

#Se toman las siguientes variables
transformarADias = (dia1 + mes1 * 30 + anio1 * 365) #cantidad considerable de dias (dias)
transformarADias2 = (dia2 + mes2 * 30 + anio2 * 365)#cantidad considerable de dias (dias)

#Ahora se realizan las operaciones
diferenciaFechas = abs(transformarADias2 - transformarADias)


#Ahora se transforma esta diferencia
años = diferenciaFechas // 365
diferenciaFechas %= 365
meses = diferenciaFechas // 30
dias = diferenciaFechas % 30
#Se vuelve a transformar a dias

#'13101997'

print(f"La diferencia entre las fechas es: {años} años, {meses} meses y {dias} días")


#Traza
#fecha1 = '13-10-1997'
#fecha2 = '13-10-2024'

#Remover cosas ("-")
#listaFecha1 = fecha1.split("-")
#listaFecha2 = fecha2.split("-")

#Ya las cosas fueron removidas
#listaFecha1 = '13101997'
#listaFecha2 = '13102024'


#Conversion de str a int

#dia1 = '13'-------->(13)
#mes1 = '10'-------->(10)
#anio1 = '1997'----->(1997)

#dia2 = '13'-------->(13)
#mes2 = '10'-------->(10)
#anio2 = '2024'----->(2024)

#Se termina la conversion de str a int


#Se transforma todo a dias
#tranformar1 = (dia1 + mes1 * 30 + anio1 * 365)------->(13 + (10)*30 + (1997) * 365) = 729218
#tranformar2 = (dia2 + mes2 * 30 + anio2 * 365)------->(13 + (10)*30 + (2024) * 365) = 739093

#distancia = abs(739093 - 729218) = 9875


#años = (9875) // 365 = 27
#mes = (27) // 30 = 0
#dias = (27) % 30 = 0

#muestra por pantalla------> 27 0 0