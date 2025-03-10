#Sistema de elecciones
#Candidatos a tirarse: Juanito, Benja, Roberto


#Contadores
votosPorJ = 0
votosPorB = 0
votosPorR = 0

votacion_en_curso = True

while votacion_en_curso:
    candidato = input("Ingrese a su candidato favorito: ")

    #Opcion de corte del programa
    if(candidato == "Finalizar" or candidato.lower() == "finalizar"):
        votacion_en_curso = False

    if(candidato == "Juanito"):
        votosPorJ += 1
    elif(candidato == "Benja"):
        votosPorB += 1
    elif(candidato == "Roberto"):
        votosPorR +=1
    

if(votosPorJ == votosPorR == votosPorB):
    print("Se declara como empate")

elif(votosPorJ > votosPorB and votosPorJ > votosPorR):
    print(f"El ganador de esta contienda es Juanito por {votosPorJ} votos")

elif(votosPorB > votosPorJ and votosPorB > votosPorR):
    print(f"El ganador de esta contienda es Benja por {votosPorB} votos")

elif(votosPorR > votosPorJ and votosPorR > votosPorB):
    print(f"El ganador de esta contienda es Roberto por {votosPorR} votos")