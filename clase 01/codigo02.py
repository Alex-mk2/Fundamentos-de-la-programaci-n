



#Ejercicio n°2: Cree un programa en python en que se pueda mostrar que tipo de triangulo es


#Ingreso por pantalla de los tres lados de un triangulo
lado1 = int(input("Ingrese el primer lado: "))

#Ingreso del segundo lado
lado2 = int(input("Ingrese el segundo lado: "))

#Ingreso del tercer lado
lado3 = int(input("Ingrese el tercer lado: "))


#Como los numeros no pueden ser negativos
if(lado1 & lado2 & lado3 < 0):
    print("Los lados negativos no existen")


#Luego se genera la condicion para saber que tipo de triangulo es
if(lado1 == lado2 == lado3):
    print("Se tiene un triangulo equilatero")
elif(lado1 == lado2):
    print("Se tiene un triangulo isoceles")
else:
    print("Se tiene un triangulo escaleno")

#Se imprime por pantalla que tipo de triangulo es