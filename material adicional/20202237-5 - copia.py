#FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA/FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
#SECCIÓN DEL CURSO: L-33
#PROFESOR DE TEORÍA: JOSÉ GONZÁLEZ
#PROFESOR DE LABORATORIO: DANIEL CALDERÓN
#
#AUTOR 
#NOMBRE: BASTIÁN MAUREIRA
#RUN: 20.202.237-5
#CARRERA: INGENIERÍA CIVIL MECATRÓNICA
#

#Variables globales: Variables que no cambiaran con el tiempo
MINUSCULAS = "abcdefghijklmnñopqrstuvwxyz"
MAYUSCULAS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
NUMEROS = "0123456789"
#Fin variables globales



# Se crea una bandera para cortar el bucle
finalizar = True

# PROCESAMIENTO
while finalizar:
    # Se le pide al usuario que ingrese una contraseña
    contrasena = input("Ingrese una contraseña: ")
    
    # Si la contraseña es "terminar", el ciclo se detiene
    if contrasena.lower() == "terminar":
        print("Se termina ejecucion del programa")
        finalizar = False
    else:
        # Se definen las variables
        c = ","
        pc = ";"
        string = ""
        
        # Verificar si la contraseña tiene al menos una minúscula
        for carac in contrasena:
            a = carac
            if a in MINUSCULAS:
                string = string + a
        
        if len(string) == 0:  # No tiene minúscula
            print("Debe tener al menos una minúscula.")
        else:
            string = ""
            # Verificar si la contraseña tiene al menos una mayúscula
            for carac in contrasena:
                a = carac
                if a in MAYUSCULAS:
                    string = string + a
            
            if len(string) == 0:  # No tiene mayúscula
                print("Debe tener al menos una mayúscula.")
            else:
                string = ""
                # Verificar si la contraseña tiene al menos una letra (mayúscula o minúscula)
                for carac in contrasena:
                    a = carac
                    if a in MINUSCULAS or a in MAYUSCULAS:
                        string = string + a
                
                if len(string) == 0:  # No tiene letras
                    print("Debe tener al menos una letra.")
                else:
                    string = ""
                    # Verificar si la contraseña tiene al menos un dígito
                    for carac in contrasena:
                        a = carac
                        if a in NUMEROS:
                            string = string + a
                    
                    if len(string) == 0:  # No tiene dígito
                        print("Debe tener al menos un dígito.")
                    else:
                        string = ""
                        # Verificar si la contraseña tiene al menos una coma
                        for carac in contrasena:
                            a = carac
                            if a in c:
                                string = string + a
                        
                        if len(string) == 0:  # No tiene coma
                            print("Debe tener al menos una coma.")
                        else:
                            string = ""
                            # Verificar si la contraseña tiene al menos un punto y coma
                            for carac in contrasena:
                                a = carac
                                if(a in pc):
                                    string = string + a
                            
                            if len(string) == 0:  # No tiene punto y coma
                                print("Debe tener al menos un punto y coma.")
                            else:
                                print("Su password cumple con todas las reglas.")
    
    
