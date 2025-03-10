

#Ejercicio de tipo prueba

#2-2018


#Definicion de funciones

#Descripcion: Funcion para poder retroceder la hora
#Dom: hora, segundosRetroceder
#Recorrido: hora 

#Fin definicion de funciones

#Procedimiento 


#HH:MM:SS--------> ":"---------->Horas = "HHMMSS"

#1 hora: 60 min---> 1 min = 60 seg-----> 1 hora en segundos = 3600 


def retrocederHora(hora, segundosRetroceder):
    listaHora = hora.split(":") #Quitamos los puntos para separar el contenido de una lista de horas
    hora = int(listaHora[0]) #Aqui serían las horas
    minuto = int(listaHora[1]) #Aqui serian los minutos
    segundo = int(listaHora[2]) #Aqui se toman los segundos
    #Principal lo que realiza
    segundosTotales = (hora * 3600 + minuto * 60 + segundo) - segundosRetroceder #Se convierte a segundos
    if(segundosTotales < 0):
        return "00:00:00"
    else:
        stringHora = "" #hora = 1
        horas = segundosTotales // 3600 #Se convierte a horas
        if(horas < 10): #Si es menor a 10 horas
            stringHora = "0" + str(horas) + ":" #3420 // 3600----> "00:"
        else:
            stringHora = str(horas) + ":" #Se convierte a horas y se agrega los puntos
        minutos = (segundosTotales % 3600) //60 # (3420 % 3600) //60
        if(minutos < 10): #Si es menor a 10 min #
            stringHora += "0" + str(minutos) + ":" #minutos = "00:"--->
        else:
            stringHora += str(minutos) + ":"
        segundos = (segundosTotales % 3600) % 60 #Transformar a segundos #(3420 % 3600) % 60
        if(segundos < 10):
            stringHora += "0" + str(segundos) 
        else:
            stringHora += str(segundos)
        return stringHora


#Traza de la funcion
#stringHora = ""
#hora = 01:00:00
#segundosAretroceder: 180-----> 3 minutos

#Caso 1 hora
#hora = "01:"

#Caso 2 minutos
#minutos 
#stringHora = "01:00:"

#Caso 3 segundos
#Segundos
#stringHora = "01:00:00"


#Para el caso que no se haya restado nada


#Primera parte



#----------------------------------------------------------------------------------#


#Si ahora se le resta algo
#segundosAretroceder =180----->3 minutos


#segundosTotales = 3600 - 180 = 3420 segundos

#Traza de la funcion
#stringHora = ""
#hora = 01:00:00
#segundosAretroceder: 180-----> 3 minutos

#Caso 1 hora
#hora = "01:"

#Caso 2 minutos
#minutos 
#stringHora = "01:00:"

#Caso 3 segundos
#Segundos
#stringHora = "01:00:00"





#Menu principal

hora = input("Ingrese la hora en formato HH:MM:SS: ")
segundosARetroceder = int(input("Ingrese segundos a retroceder: "))
retrocederHora = retrocederHora(hora, segundosARetroceder)
print(retrocederHora) 