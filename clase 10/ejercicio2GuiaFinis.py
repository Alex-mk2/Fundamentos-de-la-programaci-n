

#Se realiza por ingreso de pantalla los siguientes parametros
anioActual = int(input("Ingrese el año actual: "))
anioEgreso = int(input("Ingrese el año de egreso: "))

#Adicional a esa informacion se tiene que la edad aproximada de un estudiante son 18 años
estudiante = 18

if(estudiante != 0):
    rangoMin = (anioActual - anioEgreso + 5 + estudiante) 
    rangoMax = (anioActual - anioEgreso + 7 + estudiante) 
    print(f"La edad aproximada del estudiante esta entre {rangoMin} y {rangoMax}")
print("Se ha detenido la ejecucion del programa")