#Se requieren 10 estudiantes
#Deben cumplir un requisito en comun, altura >= 1.80 mt
#Se escogen a solo 5 personas que cumplan ese requisito

#Primero, se debe hacer un llenado con lista para almacenar los estudiantes con ese requisito

#Se crea un iterador
i = 0

#Se crea una lista con los estudiantes
lista_estudiantes = [] 

#Se crea una lista con los estudiantes candidatos
candidatos = [] #vacia------> len(candidatos) = 0 #candidatos = [1,2,3]----> len(candidatos) = 3

#Se crea una lista de reservas en caso de que superen los candidatos
reservas = []

#Se crea una variable contador
contador = 0

#Caso para llenar una lista con 10 estudiantes
while(len(lista_estudiantes) < 10):
    altura_estudiantes = int(input("Ingrese la altura de los estudiantes: ")) #[192, 183, 182, 184]
    lista_estudiantes.append(altura_estudiantes)


#Ahora se recorre la lista que se lleno con estudiantes de distintas alturas y se busca los que cumplan el requisito
while(i < len(lista_estudiantes)):
    if(lista_estudiantes[i] >= 180 and len(candidatos) < 5): #lista_estudiantes[1] = 182, len(candidatos) = 1
        candidatos.append(lista_estudiantes[i])
        contador = contador + 1
    
    elif(lista_estudiantes[i] >= 180 and len(candidatos) >= 5):
        reservas.append(lista_estudiantes[i])
    i = i + 1


#Se crea la estructura para contar los candidatos en caso de que no hayan los suficientes
restantes = 5 - len(candidatos) #5 - 2 = 3

if(restantes > 0):
    print(f"Faltan candidatos {restantes} restantes")


#Impresiones por pantalla

print("Muestrame los 5 mejores candidatos en altura", candidatos)
print("Muestrame las reservas que hay para el equipo: ", reservas)


#Traza del programa
#2 alturas = (192, 182)
#lista_estudiantes = [192, 182]
#i = 0
#candidatos = [192]
#contador = 1


#Segundo ciclo
#2 alturas = (192,182)
#lista_estudiantes = [192,182]
#i = 1
#candidatos = [192, 182]
#contador = 2

#Tercer ciclo
#2 alturas = (192,182)
#lista_estudiantes = [192,182]
#i = 3
#candidatos = [192, 182]
#contador = 2

#Usuario ingresa = 150 (valor descartado)