#Ejercicio laboratorio 2



#Se crea 2 variables para acumular
jugadores =  0
jugadores_banca = 0

#Se define un iterador, ya que necesitamos recorrer el ciclo
i = 1 #Parte del 1, ya que se va cpntar del 1 hasta 10 jugadores

#Mientras el iterador sea menor o igual que 10
while(i <= 10):
    #Obs: Se necesita que aqui ingrese la altura (ya que deben iterarla 10 veces)
    altura = float(input("Ingrese una estatura: ")) 
#Se crea la primera condición 
    if(altura > 1.80):
        #Incrementamos el iterador
        jugadores = jugadores + 1
        #también se incrementa el contador
    i = i + 1 #Observaciones: Iterador debe ir afuera del if

#Segunda condición para los jugadores tituales y para la banca

#Si jugadoes es mayor o igual a 5
#Cuando ya superen el n°o de jugadores ( los 5 candidatos, se debe mostrar equipo completo)
if(jugadores >= 5):
    print("Equipo titular completo") #muestra por pantalla equipo titular
    #Se le resta 5 a jugadores ya que el resto quedaria en la banca
    #Ya que son 10 en total y 5 debes titular y los 5 de suplentes
    jugadores_banca = jugadores - 5
    print("Jugadores a la banca:", jugadores_banca)
#Si no se cumplen ambas condiciones, se debe mostrar que faltan jugadores
else:
    jugadores_faltantes = 5 - jugadores_banca
    print("Faltan", jugadores_faltantes, "jugadores")