
#Pangrama (es decir, no se repite en ninguna de sus letras y utiliza todas las letras del abecedario)

#Ejemplos de pangramas: 
#Fabio me exige, sin tapujos, que añada cerveza al whisky 
#Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol

#Es necesario el abecedario para hacer la comparacion

abecedario = 'abcdefghijklmnopqrstuvwxyz'

#Ingresar el pangrama por pantalla, y que sea minuscula para eso nos aseguramos con lower()
pangrama = str(input("Ingrese un pangrama: ")).lower()

#Se crea un iterador, ya que necesitamos recorrer 
contador = 0 

#Se crea una bandera para saber cuando termina el proceso
bandera = False #flag = TRUE #flag = FALSE #logica booleana true = 0, false = 1

#Ejemplo interruptor (encender o apagar)
#Se itera hasta el larga del abecedario, para eso se utiliza len que nos da el largo.

#len = devuelve el largo de la lista de elementos

while(contador < len(abecedario)):
    if(abecedario[contador] not in pangrama): #Si el pangrama ingresado por el usuario no se encuentra en abecedario (recorrido por su contador)
        #Asignamos la bandera como verdadero, ya que no se repite ninguna de las letras
        bandera = True
    #Incrementamos el contador
    contador = contador + 1 #z, este while se va a romper

#contador = 0    #contador = 1   #contador = 2  #contador = 3  #contador = 4  
#abecedario = a  #abecedario = b #abecedario = c #abecedario = d #abecedario = e

#Salimos del ciclo y hacemos las verificaciones

if(bandera == False):
    #Indicamos que si es un pangrama
    print("Si es un pangrama")
else:
    print("No es un pangrama")



