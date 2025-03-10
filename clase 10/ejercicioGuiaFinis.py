

#Evaluacion de estudiantes

#Ingreso de nota de estudiante por pantalla
estudiante = float(input("Ingrese su nota: "))

while(estudiante != 0):
    if(1.0 <= estudiante < 4.0):
        print(f"El estudiante ha reprobado el ramo con un {estudiante}")
    elif(4.0 <= estudiante < 5.5):
        print(f"El estudiante ha aprobado el ramo con un {estudiante}")
    elif(5.5 <= estudiante <= 7.0):
        print(f"El estudiante se ha eximido del ramo con un {estudiante}")
    else:
        print("Ingreso incorrecto de notas")
    
    estudiante = float(input("Ingrese otra nota o 0 para finalizar el programa: "))

print("Se ha detenido el programa") 

