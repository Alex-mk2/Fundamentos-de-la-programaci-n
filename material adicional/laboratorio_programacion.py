"""
--------------------------------------------------------------------------------
Laboratorio Conjuntos de Datos
--------------------------------------------------------------------------------

El siguiente conjunto de datos (datos_climaticos), posee información climática
recopilada por diferentes sensores ambientales (humedad y temperatura) durante
un mes completo.

El detalle de los datos es el siguiente:

  día     : Identifica el día en el cual se registraron los datos.
  temp_min: Registro de la temperatura más baja del día.
  humd_min: Registro de la humedad más baja del día.
  temp_max: Registro de la temperatura más alta del día.
  humd_max: Registro de la humedad más alta del día.


Actividad 1:
------------

Escriba un programa en Python, que logre generar un informe que contenga los siguientes
indicadores:

  1.- La temperatura más baja y el día en que se registró.
  2.- La temperatura más alta y el día en que se registró.
  3.- La humedad más baja y el día en que se registró.
  4.- La humedad más alta y el día en que se registró.
  5.- El promedio de temperatura del mes.
  6.- El promedio de humedad del mes.
  7.- El listado de días para los cuales, la oscilación térmica fue superior a 15 grados.
  8.- El listado de días para los cuales, la oscilación de humedad fue superior a 50%.

"""

datos_climaticos = (
    {'dia': 1,  'temp_min': 5,  'humd_min': 48, 'temp_max': 22, 'humd_max': 99},
    {'dia': 2,  'temp_min': 1,  'humd_min': 43, 'temp_max': 23, 'humd_max': 92},
    {'dia': 3,  'temp_min': -4, 'humd_min': 98, 'temp_max': 6,  'humd_max': 99},
    {'dia': 4,  'temp_min': 11, 'humd_min': 30, 'temp_max': 17, 'humd_max': 36},
    {'dia': 5,  'temp_min': 22, 'humd_min': 86, 'temp_max': 24, 'humd_max': 99},
    {'dia': 6,  'temp_min': 0,  'humd_min': 37, 'temp_max': 6,  'humd_max': 80},
    {'dia': 7,  'temp_min': 3,  'humd_min': 43, 'temp_max': 11, 'humd_max': 96},
    {'dia': 8,  'temp_min': 17, 'humd_min': 14, 'temp_max': 25, 'humd_max': 44},
    {'dia': 9,  'temp_min': 3,  'humd_min': 32, 'temp_max': 11, 'humd_max': 64},
    {'dia': 10, 'temp_min': 8,  'humd_min': 21, 'temp_max': 18, 'humd_max': 99},
    {'dia': 11, 'temp_min': 15, 'humd_min': 57, 'temp_max': 20, 'humd_max': 91},
    {'dia': 12, 'temp_min': 20, 'humd_min': 33, 'temp_max': 23, 'humd_max': 87},
    {'dia': 13, 'temp_min': -2, 'humd_min': 83, 'temp_max': 3,  'humd_max': 98},
    {'dia': 14, 'temp_min': 17, 'humd_min': 55, 'temp_max': 18, 'humd_max': 80},
    {'dia': 15, 'temp_min': 14, 'humd_min': 56, 'temp_max': 24, 'humd_max': 61},
    {'dia': 16, 'temp_min': 1,  'humd_min': 65, 'temp_max': 23, 'humd_max': 68},
    {'dia': 17, 'temp_min': 23, 'humd_min': 77, 'temp_max': 23, 'humd_max': 79},
    {'dia': 18, 'temp_min': 1,  'humd_min': 51, 'temp_max': 14, 'humd_max': 82},
    {'dia': 19, 'temp_min': 5,  'humd_min': 59, 'temp_max': 5,  'humd_max': 66},
    {'dia': 20, 'temp_min': 22, 'humd_min': 28, 'temp_max': 24, 'humd_max': 97},
    {'dia': 21, 'temp_min': 13, 'humd_min': 48, 'temp_max': 25, 'humd_max': 99},
    {'dia': 22, 'temp_min': 16, 'humd_min': 52, 'temp_max': 16, 'humd_max': 58},
    {'dia': 23, 'temp_min': -4, 'humd_min': 47, 'temp_max': 1,  'humd_max': 72},
    {'dia': 24, 'temp_min': 3,  'humd_min': 18, 'temp_max': 25, 'humd_max': 71},
    {'dia': 25, 'temp_min': 23, 'humd_min': 49, 'temp_max': 23, 'humd_max': 66},
    {'dia': 26, 'temp_min': 6,  'humd_min': 10, 'temp_max': 23, 'humd_max': 27},
    {'dia': 27, 'temp_min': 20, 'humd_min': 73, 'temp_max': 25, 'humd_max': 76},
    {'dia': 28, 'temp_min': 3,  'humd_min': 74, 'temp_max': 17, 'humd_max': 74},
    {'dia': 29, 'temp_min': 6,  'humd_min': 33, 'temp_max': 25, 'humd_max': 48},
    {'dia': 30, 'temp_min': 1,  'humd_min': 68, 'temp_max': 23, 'humd_max': 74}
)


#Para encontrar la temperatura más baja y dia bastaria recorrer esta data
minTemp = 101
dia = 0
#Para eso utilizaremos la estructura que nos ofrece for (en este caso al ser tuplas de diccionarios se debe recorrer de esta forma)
for d1 in datos_climaticos:
    if(d1["temp_min"] < minTemp):
        min = d1["temp_min"]
        dia = d1["dia"]
print(f"La temperatura minima y dia registrados son {minTemp} y {dia}")


#Ahora para buscar el maximo dentro de esta estructura de diccionarios
maxTemp = -1
diaMax = -1
for d1 in datos_climaticos:
    if(d1['temp_max'] > maxTemp):
        max = d1['temp_max']
        diaMax = d1['dia']
print(f"La temperatura maxima y dia registrados son {maxTemp} y {diaMax}")


#Ahora para buscar la humedad mas baja es necesario tomar los siguientes datos
#Como nota adicional, si se quiere buscar el minimo valor en vez de none utilicen un valor más alto
minHum = 101
for d1 in datos_climaticos:
    if(d1['humd_min'] < minHum):
        minHum = d1['humd_min']
        dia = d1['dia']
print(f"La humedad minima y dia registrados son {minHum} y {dia}")

#Ahora mismo, para la humedad maxima
#Observaciones: Al final se va revisando por "etiquetas", los recorridos y demás funcionalidades al ser tuplas no se puede
#aplicar funciones
maxHum = -1
for d1 in datos_climaticos:
    if(d1['humd_max'] > maxHum):
        maxHum = d1['humd_max']
        dia = d1['dia']
print(f"La humedad maxima y dia registrados son {maxHum} y {dia}")

#Ahora para obtener el promedio del mes
largoLista = 0
largoLista2 = 0

#Se cuentan estos datos
datos_max = 0
datos_min = 0

#Se define un promedio para minTemp y maxTemp
promedioMin = 0
promedioMax = 0

for d1 in datos_climaticos:
    largoLista = d1['temp_max']
    largoLista2 = d1['temp_min']
    datos_max = datos_max + 1 #Se incrementan los datos
    datos_min = datos_min + 1 
    promedioMin = d1['temp_max'] / datos_max
    promedioMax = d1['temp_min'] / datos_min

print(promedioMin + promedioMax) #Se suman ambos promedios, ya que piden temperatura en general del mes


#El siguiente ejercicio lo dejaré para realizar...