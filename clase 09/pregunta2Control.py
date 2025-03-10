#Cree un programa que permita la multiplicacion de dos numeros
#Restricciones: No se puede utilizar las operaciones para multiplicar (**, *, /, //, %)

#En teoria se debe hacer por sumas (Cuando se dice por sumas implica utilizar un while)

#Se pide por pantalla el numero
numero = int(input("Ingrese un numero: "))
numero1 = int(input("Ingrese un segundo numero: "))

#Se crea un iterador
i = 0

#Se crea una variable para almacenar el resultado
resultado = 0

#Mientras no alcance el largo de alguno de los numeros (suma de sumas)----->while(componentes i, j = 0 hasta n)
while(i < numero): # 3 < 3
    resultado+= numero1  #resultado = 6 + (numero1 = 3)------> resultado = 9
    i = i + 1

print(f"La suma de los numeros es {resultado}")

#Traza del programa
#numero = 3
#numero1 = 3
#i = 0
#resultado = 3


#Segunda iteracion
#numero = 3
#numero1 = 3
#i = 1
#resultado = 6

#Tercera iteracion
#numero = 3
#numero1 = 3
#i = 2
#resultado = 9

#Cuarta iteracion
#numero = 3
#numero1 = 3
#i = 3
#resultado = 9