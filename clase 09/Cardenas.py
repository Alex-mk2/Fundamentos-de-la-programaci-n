#laboratorio n °2
#Ejercicio 1 Control de flujo condicional 

#Se crea un menu solicitando los años de carrera 
aniosPostgrado = int(input("Ingrese los años de postgrado (maximo 5 años"))
# Solicitar al usuario ingresar 5 notas y validarlas
nota1 = float(input("Ingrese la primera nota (entre 1.0 y 7.0)"))
#Se usa un ciclo while para validar la primera nota
while(nota1 < 1.0 or nota > 7.0):
    print("Nota incorrecta ingrese en el formato (1.0 y 7.0)")
#se incrementa el contador 
suma_notas = suma_notas + nota1
#Segunda nota
nota2 = float(input("Ingrese la segunda nota (entre 1.0 y 7.0)"))
while(nota2 < 1.0 or nota > 7.0):
    print("Nota incorrecta ingrese en el formato (1.0 y 7.0)")
suma_notas = suma_notas + nota2
#Tercer nota
nota3 = float(input("Ingrese la tercera nota (entre 1.0 y 7.0)"))
while(nota3 < 1.0 or nota > 7.0):
    print("Nota incorrecta ingrese en el formato (1.0 y 7.0)")
suma_notas = suma_notas + nota3
#Cuarta nota
nota4 = float(input("Ingrese la cuarta nota (entre 1.0 y 7.0)"))
while(nota3 < 1.0 or nota > 7.0):
    print("Nota incorrecta ingrese en el formato (1.0 y 7.0)")
suma_notas = suma_notas + nota1
#Quinta nota
nota5 = float(input("Ingrese la quinta nota (entre 1.0 y 7.0)"))
while(nota3 < 1.0 or nota > 7.0):
    print("Nota incorrecta ingrese en el formato (1.0 y 7.0)")
suma_notas = suma_notas + nota5

# Si todas las notas son validas se calcula el promedio de las notas
promedio = suma_notas / 5
print("El promedio de las notas es", promedio)

# Se determinan las notas segun su beca
if(promedio > 6.0):
    beca = 3000000
    print("Beca completa")
elif(5.5 <= promedio < 6.0):
    beca = 1000000 
    print("Beca parcial")
elif(5.0 <= promedio < 5.5):
    beca = 500000 
    print("Beca minima")
else:
    beca = 0
    print("No posee beca")
print("La beca le cubrira: ", beca * aniosPostgrado)
