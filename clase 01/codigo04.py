

#Ejercicio n°4 sumatoria de Gauss en Python

#Primero necesitamos el número ingresado
numero = int(input('Ingrese un número: '))

#Necesitamos un contador o iterador para realizar la sumatoria
contador = 1
sumatoria = 0

#Se recorre desde el contador hasta el numero ingresado (toma desde 1 hasta n veces)
while(contador <= numero):
    # Se suma cada valor del contador a la sumatoria
    sumatoria += contador
    #Se incrementa el contador
    contador += 1

#Se muestra por pantalla la sumatoria
print('La sumatoria es:', sumatoria)

#Gauss numero = n(n + 1)/2
#Gauss de 5 = 5(5 + 1)/2 = 15
#Gauss de 0 = 0(0 + 1)/2 = 0

