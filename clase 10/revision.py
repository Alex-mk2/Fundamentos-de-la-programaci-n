# Solicitar dos números al usuario
inicio = int(input("Ingrese un número de inicio: ")) # 2
fin = int(input("Ingrese un número final: ")) # 3

# Ciclo para recorrer todos los números
while inicio <= fin:
    # Se crea un contador para cada número
    contador = 0
    # Se crea un iterador para cada número
    i = 1

    # Verificamos si el número actual es primo
    while i <= inicio:
        # Si el número es divisible por i que es 1
        if inicio % i == 0:
            # Incrementamos el contador
            contador = contador + 1
        # Incrementamos el iterador
        i = i + 1

    # Si el contador es igual a 2, el número es primo (divisible por 1 y por sí mismo)
    if contador == 2:
        print(inicio, "es primo")
    
    
    # Incrementamos el número para verificar el siguiente
    inicio = inicio + 1