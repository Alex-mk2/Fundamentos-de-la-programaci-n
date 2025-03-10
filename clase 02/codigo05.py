#Ejercicios arboles, de tipo pep


#Este ejercicio fue de una prueba que yo dí en su tiempo


#Se tienen las cuatro estaciones del año, verano, otoño, invierno, primavera


#Se tiene la siguiente información respecto a las estaciones 
#Primavera aumenta un 30% ----> 0.3
#Verano aumenta 1 metro -----> 100 cm
#Otoño aumenta en 5% -----> 0.05
#Invierno no crece------> 0

#Consideraciones adicionales

#Todos los arboles se plantan en primavera
#Comienzan con una altura de 0.5
#Cada estación dura 3 meses
#Requiere como entrada valor de altura
#Solo numeros positivos


#Constantes del programa (todos en mt)

DURACION_ESTACION = 3
PRIMAVERA = 0.3
OTONO = 0.05
VERANO = 1
INVIERNO = 0

#Fin de constantes del programa

#int = 1, 3, 5, 7, 8
#float = 1.0, 1.5, 2.8, 3.5

#Inicio del programa

altura = abs(float(input("Ingrese una altura en metros: ")))

#Cada arbol inicia con 0.5 de altura
alturaInicial = 0.5

#Se inicia en el mes 0 (se asume que en primavera)

mes = 0

#Se comienza con primavera, aquí se utilizará booleanos para representar el estado vigente de cada mes o mes activo
primavera = True
otono = False
invierno = False
verano = False

#Se inicia con el ciclo while


#Traza del programa

#Operaciones matematicas
#para primavera
#alturaInicial = 0.5, alturaInicial = 0.5 + 0.5 * 0.3 (PRIMAVERA), alturaInicial = 0.65


#para verano
#alturaInicial = 0.65, alturaInicial = 0.65 + 0.65 * 1 (verano), alturaInicial = 1.3

#Para otoño
#alturaInicial = 1.3, alturaInicial = 1.3 + (1.3 * 0.05), alturaInicial = 1.365

#Para invierno
#alturaInicial = 1.365, alturaInicial = 1.365

#altura = 2.0
#primavera = true, falso, falso, falso, verdadero
#verano = falso, verdadero, falso, falso, falso
#otoño = falso, falso, verdadero, falso, falso
#invierno = falso, falso, falso, verdadero, falso
#mes = 0, 3, 6, 9, 12

while (alturaInicial <= altura): #0.5 <= 2.0
    #Si es primavera
    if (primavera): #si primavera es verdadero
        #Si la altura inicial es menor que la altura
        if (alturaInicial <= altura):

            #Se le suma la altura en primavera
            alturaInicial = alturaInicial + alturaInicial * PRIMAVERA

            #Aumenta el contador de meses
            mes+=3

            #Se cambia el estado de los meses, pasa al siguente

            verano = True #si es verdadero verano
            primavera = False #primavera es falso
    
    if(verano):

        #Misma logica que el anterior caso
        if(alturaInicial <= altura): #0.65 <= 2.0

            #Ahora se le suma lo que crece en verano
            alturaInicial = alturaInicial + alturaInicial * VERANO #1.3

            #Aumenta el contador de meses
            mes+=3

            #Se cambia el estado de los meses, ahora nos vamos a otoño

            verano = False
            otono = True

    if(otono):

        #Misma logica
        if(alturaInicial <= altura): #1.3 <= 2.0

            #Ahora se le suma lo de otoño

            alturaInicial = alturaInicial + alturaInicial * OTONO #1.365

            #Aumenta contador de meses

            mes+=3

            #Se cambia el estado al siguiente mes

            otono = False
            invierno = True


    if(invierno):
        #Misma logica

        if(alturaInicial <= altura): #1.365 <= 2.0

            #Como invierno no crece queda lo siguiente

            alturaInicial = alturaInicial + alturaInicial * INVIERNO #(0), #1.365

            #Seteo mes

            mes+=3

            #Cambio de estado

            invierno = False
            primavera = True

print("El tiempo que demora en crecer la altura", alturaInicial, "en tantos meses es", mes)