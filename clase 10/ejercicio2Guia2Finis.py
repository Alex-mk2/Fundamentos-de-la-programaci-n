


#Se crea un contador para el ingreso de asignaturas
contadorAsignaturas = 0

#Se crea un validador para finalizar
agregarNotas = True

#Suma notas
sumaNotas = 0

#Suma pesos
pesos = 0

#Promedio
promedio = 0


while(agregarNotas): #agregarNotas = False
    asignatura = input("¿Desea agregar una asignatura? (Si/No): ")
    if(asignatura == "N" or asignatura.lower() == "n"):
        agregarNotas = False
    else:
        calificacion = float(input("Ingrese su calificacion: "))
        creditos = int(input("Ingrese los creditos de esa asignatura: "))

        #Como se esta agregando informacion se cuenta (asignatura, calificacion, creditos)
        contadorAsignaturas = contadorAsignaturas + 1 #(asignatura, calificacion, creditos)-------> se cuenta como 1
        sumaNotas+= calificacion * creditos
        pesos+= creditos

#Luego para calcular el promedio
if(contadorAsignaturas > 0): #contadorAsignatura = 2--------> (2 > 0)
    promedio = (sumaNotas  / pesos)


print("***Resultados***")
print(f"El promedio obtenido es {promedio}")
print(f"La cantidad de asignaturas inscritas son {contadorAsignaturas}")


#promedio = (sumaNotas / cantidadNotas)
#promedio ponderado = (sumaNotas * peso / peso)


#Traza programa
#asignatura: Si
#calificacion: 7.0
#creditos: 7
#contadorAsignaturas: 1
#pesos = 7
#sumaNotas = (7.0 * 7)


#"Segundo ciclo"
#asignatura: Si
#califacion: 6.0
#creditos: 5
#contadorAsignaturas: 2
#pesos = 7 + 5 ------> 12
#sumaNotas = (7.0 * 7 + 6.0 * 5)


#contadorAsignaturas > 0
#promedio = (7.0 * 7 + 6.0 * 5)/ pesos = 12
#promedio = (7.0 * 7 + 6.0 * 5) / 12
#promedio = 6.583....


#*******************************Primer ciclo y segundo**********************************************


#"Tercer ciclo"
#asignatura: N


