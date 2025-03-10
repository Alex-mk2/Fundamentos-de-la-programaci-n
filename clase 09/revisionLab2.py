

#Contruir un sistema de becas para la u finis

#Se requiere que se ingresen notas que sean validas
notasValidas = 0

#Se requiere un iterador
i = 0

#variable para la suma de notas
sumaNotas = 0

#Variable para el promedio de notas
promedio = 0

#Variable para la beca
beca = 0

while notasValidas != 5:
    aniosPostgrado = int(input("Ingrese los años de postgrado (maximo 5 años): "))
    if(aniosPostgrado < 0 or aniosPostgrado > 5):
        print("No pueden existir años negativos y no puede pasarse de los 5 años")
    else:
        notasValidas = 0
        #Con esto se tiene que nunca va a exceder de los 5 años maximo del postgrado
        while(i < aniosPostgrado):
            notasPregrado = int(input("Ingrese 5 notas que sean validas: "))
            if(10 <= notasPregrado <= 70):
                print("Nota ingresada correctamente")
                sumaNotas +=notasPregrado 
                notasValidas = notasValidas + 1
            else:
                print("Formato incorrecto de notas")
                break
            i = i + 1
        if(notasValidas == 5):
            print("Notas correctas ingresadas")
            break

#Para calcular el promedio, nos bastaria verificar si las notas que fueron ingresadas son correctas
if(notasValidas > 0):
    promedio = (sumaNotas / notasValidas)
else:
    promedio = 0

if(promedio >= 60):
    beca= 3000000
elif(55 <= promedio < 60):
    beca= 1000000
elif(50 <= promedio < 55):
    beca=500000
else:
    beca = 0


print(f"El promedio de notas es {promedio}")
print(f"La beca le cubrira {beca * aniosPostgrado} durante los 5 años")