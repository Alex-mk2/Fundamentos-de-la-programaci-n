#Prueba de diversos ejercicios de condicionales




# Ejercicio n°1: Compra y venta de alcohol en Python (Ejercicio para comprender)

#Ingreso de edad por pantalla, un numero entero
#Recordar también la primitiva de int (entero)
edad = int(input("Ingrese una edad: "))

#Ejemplo de una condición simple
if (edad >= 18):
    print("Edad legal para comprar alcohol")
elif (edad == 17):
    print("Necesita mostrar el carnet para comprar")
else:
    print("Es menor de edad, prohibido el consumo de bebidas alcohólicas")
