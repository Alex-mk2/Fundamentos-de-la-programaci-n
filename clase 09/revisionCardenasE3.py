from random import randint
num_aleatorio = randint(1, 100)

# Inicialización del saldo total
saldo_total = 0

# Ciclo principal del juego

seguir_jugando = "s"
while seguir_jugando == "s" or seguir_jugando == "S":
    
# Solicitar la apuesta al usuario

    apuesta_valida = False
    while apuesta_valida == False:
        apuesta = input("¿Cuánto dinero deseas apostar? ")
        if apuesta.isdigit() and int(apuesta) > 0:
            apuesta = int(apuesta)
            apuesta_valida = True
        else:
            print("Por favor, ingresa un número válido mayor que 0.")
    
# Número mágico ya ha sido generado en la línea 2

    print("Se ha generado un número mágico entre 1 y 100.")

# Ciclo de 3 intentos

    acertado = False
    for intentos in range(1, 4):
        intento_valido = False
        while intento_valido == False:
            intento_usuario = input("Intento " + str(intentos) + ": Ingresa un número entre 1 y 100: ")
            if intento_usuario.isdigit() and 1 <= int(intento_usuario) <= 100:
                intento_usuario = int(intento_usuario)
                intento_valido = True
            else:
                print("El número debe estar entre 1 y 100.")
        
# Comparar el número ingresado con el número mágico

        if intento_usuario == num_aleatorio:
            acertado = True
            if intentos == 1:
                premio = apuesta * 1000
            elif intentos == 2:
                premio = apuesta * 500
            else:
                premio = apuesta * 100
            saldo_total += premio
            print("¡Felicidades! El número mágico es", num_aleatorio, ". Adivinaste en el intento", intentos, ". Has ganado", premio, "pesos.")
            intentos = 3      # Forzar la salida del ciclo for ya que acertó

        elif intento_usuario < num_aleatorio:
            print("Más arriba.")
        else:
            print("Más abajo.")

# Si no acertó

    if acertado == False:
        saldo_total -= apuesta
        print("Luego de 3 intentos, perdiste", apuesta, "pesos. El número mágico era", num_aleatorio, ".")

# Preguntar al usuario si desea seguir jugando

    seguir_jugando_valido = False
    while seguir_jugando_valido == False:
        seguir_jugando = input("¿Deseas seguir jugando? (S/N): ")
        if seguir_jugando == 's' or seguir_jugando == 'S' or seguir_jugando == 'n' or seguir_jugando == 'N':
            seguir_jugando_valido = True
        else:
            print("Por favor, ingresa 'S' para sí o 'N' para no.")

# Mostrar saldo total al terminar