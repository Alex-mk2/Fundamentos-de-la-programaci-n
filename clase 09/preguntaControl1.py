#Conversion de temperaturas

#Escriba un programa que permita convertir temperaturas en grados a farenheit o kelvin


#Ingreso de temperatura por pantalla
temperatura = int(input("Ingrese una temperatura: "))

#Se ingresa por pantalla el tipo de temperatura que desea
tipoTemperatura = input("Ingrese un tipo de temperatura (Celsius, Kelvin, Fahrenheit): ")

#Almacenamos una variable de conversion para cada temperatura
conversionAK = 0
conversionAF = 0
conversionAC = 0
#Ahora se debe realizar las decisiones del programa

if(tipoTemperatura == "Celsius"):
    conversionAK = temperatura + 273.15
    conversionAF = ((9 * temperatura)/5) + 32
    print(f"La temperatura celsius es {temperatura}")
    print(f"La temperatura celsius en Kelvin es {conversionAK}")
    print(f"La temperatura celsius en Fahrenheit es {conversionAF}")

elif(tipoTemperatura == "Fahrenheit"):
    conversionAC = (5 * (temperatura - 32)/9)
    conversionAK = (5 * (temperatura - 32)/9) + 273.15
    print(f"La temperatura en fahrenheit es {temperatura}")
    print(f"La temperatura fahrenheit en celsius es {conversionAC}")
    print(f"La temperatura fahrenheit en kelvin es {conversionAK}")
    
elif(tipoTemperatura == "Kelvin"):
    conversionAC = temperatura - 273.15
    conversionAF = (9 * (temperatura - 273.15)/5) + 32
    print(f"La temperatura en Kelvin es {temperatura}")
    print(f"La temperatura Kelvin en celsius es {conversionAC}")
    print(f"La temperatura Kelvin en fahrenheit es {conversionAF}")

else:
    print("Formato incorrecto de temperatura, abortando ejecucion")