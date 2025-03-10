#Construya un programa que entregue la cantidad de consonantes y vocales a traves de funciones



#Definicion de funciones

#Se ocupara una funcion para detectar las vocales y consonantes

#Fin definicion de funciones


#Definicion de constantes
VOCALES = 'aeiou'
CONSONANTES = 'qwrtypsdfghjklzxcvbnm'


#Funciones a diseñar
#Descripcion de la funcion: Funcion que detecta si son consonantes y vocales
#Dom: texto (el parametro)
#Recorrido: consonante si se detecta, vocal si se detecta (variables)







#Inicio funcion

def detectarVocalesyConsonantes(texto):
    #Se crean variables vocales, consonantes
    vocales = 0
    consonantes = 0
    #Se crea un iterador
    i = 0
    #Recorremos hasta el largo del texto
    while(i < len(texto)):
        #Si se encuentra en vocales
        if(texto[i] in VOCALES): #texto[3] = a, a in vocales, verdadero
            vocales+=1 #
        #Si se encuentra la letra en consonantes
        elif(texto[i] in CONSONANTES): #texto[2] = l in consonantes
            consonantes+=1 #consonantes = 2
        i = i + 1
    return (vocales, consonantes)


#Traza de la funcion

#texto = hola-----> texto[i]-------> texto[0] = h, texto[1] = o, texto[2] = l, texto[3] = a


#Primer ciclo
#i = 0
#texto = hola-----> texto[i]-------> texto[0] = h, texto[1] = o, texto[2] = l, texto[3] = a
#vocales = 0
#consonantes = 1
#texto[0] = h----> h in consonantes verdadero


#Segundo ciclo
#i = 1
#texto[1] = o
#vocales = 1
#consonantes = 1


#Tercer ciclo
#i = 2
#texto[2] = l
#vocales = 1
#consonantes = 2

#Cuarto ciclo
#i = 3
#texto[3] = a
#vocales = 2
#consonantes = 2


#Quinto ciclo
#i = 4
#texto[4] = ' '
#vocales = 2
#consonantes = 2


#Ejecucion del programa ingreso de llamados, funciones

texto = str(input("Ingrese un texto: "))
vocales, consonantes = detectarVocalesyConsonantes(texto)
print(f"La cantidad de vocales son: {vocales} y consonantes son: {consonantes}")