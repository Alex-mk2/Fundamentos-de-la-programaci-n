import random

#Se genera una lista aleatoria entre 5 a 50 
lista = list(range(random.randint(5,50)))
random.shuffle(lista)
print("Lista", lista)


#Ahora para realizar la busqueda del elemento en la lista
i = 0
resultado = []

#Mientras no llegue al largo de la lista
while(i < len(lista)):
    if(lista[i] == i):
        resultado.append(lista[i]) #elemento
    i = i + 1

print("Los elementos que coinciden son", resultado)