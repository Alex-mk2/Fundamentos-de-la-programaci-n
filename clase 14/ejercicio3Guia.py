#Diccionarios
#En este caso hay que manejar una lista de contactos (pero como diccionario, no tupla)
#Por lo cual aquí si se puede usar métodos

#Se maneja una lista de contactos

lista_contactos = {
    "Ariel": ["337/511"],
    "Natalia": ["991/117"],
    "Felix": ["355/799", "991/117"]
}

#En este caso felix maneja dos numeros


#Para este problema en particular solo requiere una funcion para el manejo de caracteres unicos


#Funcion para obtener los caracteres unicos
#Dom: lista_contactos
#Rec: caracteres

#Para este caso sera necesario el uso de un set (solo valores unicos sin importar orden)

def obtener_caracteresUnicos(lista_contactos):
    #Obtenemos los caracteres unicos sin repeticion 
    caracteres = set()
    for numeros in lista_contactos.values():
        #Se toma cada numero en lista de numeros
        for numero in numeros:
            #Se actualiza cada valor con un caracter unico
            caracteres.update(numero)
    return caracteres



#Ejecucion del programa

#Aquí se muestra la lista de contactos
print("**************Lista de contactos********************\n")

#Se toma cada elemento del diccionario a tratar
for nombre, numeros in lista_contactos.items():

    print(f"nombre: {nombre} \n numero: {','.join(numeros)}")

#Ahora se toma cada caracter unico a través de la funcion
caracter_unico = obtener_caracteresUnicos(lista_contactos)
print("\n caracteres unicos en la lista de contactos")
print(caracter_unico)

