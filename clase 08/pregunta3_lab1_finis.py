#Programa que me calcula el promedio de notas, aprobados, reprobados
#Condicion clave: > 4 aprobado, caso contrario esta reprobado



#Programa comienza solicitando la cantidad de estudiantes

estudiantes = int(input("Ingrese el numero de estudiantes: "))

#Necesitamos un contador de aprobados
contador_aprobados = 0

#Contador para los reprobados
contador_reprobados = 0

#Necesario una variable promedio
promedio = 0

#Iteradores
i = 0
j = 0
z = 0
k = 0

#Creo una lista de calificaciones por cada estudiante
lista_calificaciones = [] #----> len([]) = 0

#Crear dos variables para obtener la nota mas alta, y baja
mayor = 0

#estudiantes = 3
#calificaciones = [c1e1, c2e2, c3e3]
#Ahora lleno esa lista con las calificaciones por estudiante

while(len(lista_calificaciones) < estudiantes):
    calificaciones = int(input("Ingrese una calificacion por estudiante: "))
    if(10 <= calificaciones <= 70): 
        lista_calificaciones.append(calificaciones)
    else:
        print("Formato incorrecto de calificaciones, no cumple con la norma")

#Se recorre por calificaciones (de cada estudiante)
while(i < len(lista_calificaciones)):
    if(lista_calificaciones[i] >= 40):
        contador_aprobados = contador_aprobados + 1
    else:
        contador_reprobados = contador_reprobados + 1
    i = i + 1


#Se recorre la lista para obtener el mayor de las calificaciones
while(j < len(lista_calificaciones)):
    if(lista_calificaciones[j] > mayor):
        mayor = lista_calificaciones[j]
    j = j + 1

#Se recorre la lista para obtener el menor de las calificaciones para eso se realiza lo sgte
menor = lista_calificaciones[0] 

while(k < len(lista_calificaciones)):
    if(lista_calificaciones[k] < menor):
        menor = lista_calificaciones[k]
    k = k + 1

#Ahora se obtiene el promedio general de la clase
largoLista = len(lista_calificaciones)

#Se recorre la lista de calificaciones
while(z < len(lista_calificaciones)):
    promedio += (lista_calificaciones[z])/largoLista
    z = z + 1



print("-------------------------------Resumen de notas de los estudiantes---------------------------")
print("Muestrame los estudiantes: ", estudiantes)
print("Muestrame la lista de calificaciones: ", lista_calificaciones)
print("Muestrame los estudiantes aprobados: ", contador_aprobados)
print("Muestrame los estudiantes reprobados: ", contador_reprobados)
print("Muestrame la mejor calificacion: ", mayor)
print("Muestrame la menor calificacion: ", menor)
print("Muestrame el promedio de calificaciones: ", promedio)