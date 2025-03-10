#Ejercicio 3 Lab
#Crear un programa que calcule los promedio de notas, aprobados y reprobado
#Condicion clave: > 4 aprobado, caso contrario esta reprobado
#Inicio del programa
#Se le solicita al usuario que ingrese el número total de estudiantes en el curso
estudiantes = int(input("Ingrese numero total de estudiantes:"))

#Se crea un contador, para los aprobados
contador_aprobados = 0
#Contador para los reprobados
contador_reprobados = 0
#Conrador de estudiaintes
contador_estudiantes = 0
#Se crea un contador para la suma de calificaciones
suma_calificaciones = 0
#Se crea un iterador para la nota max y minima
calificacion_maxima = 10
calificacion_minima = 70
#Se crea un iterador 
i = 0

#Mientras la calificación sea menor al numero total de estudianres
while(contador_estudiantes < estudiantes):
    #Se crea el menu al usuario, primero necesitamos que se ingrese la calificación 
    calificacion = int(input("Ingrese una calificación por estudiante:"))
    # Se valida la calificacion en este rango entre 10 a 70 
    if(10 <= calificacion <= 70):
        suma_calificaciones = suma_calificaciones + calificacion
        contador_estudiantes = contador_estudiantes + 1
        
        #Segunda condición determinar si el estudiante aprobo o reprobó
        if(calificacion >= 40):
            contador_aprobados = contador_aprobados + 1
        else:
            contador_reprobados = contador_reprobados + 1
        #tercera condición ingresar la calificación maxima y minima
        if(calificacion > calificacion_maxima):
            calificacion_maxima = calificacion
        if(calificacion < calificacion_minima):
            calificacion_minima = calificacion
    else:
        print("Calificación inválida. Debe estar entre 10 y 70.")

#Por ultimo se calcula el promedio
promedio = suma_calificaciones/ estudiantes

#Imprimir los resultados
print("-------------------------------Resumen de notas de los estudiantes---------------------------")
print("Calificación más alta:", calificacion_maxima)
print("Calificación más baja:", calificacion_minima)
print("Promedio de notas:", promedio)
print("Número de estudiantes aprobados:", contador_aprobados)
print("Número de estudiantes reprobados:", contador_reprobados)