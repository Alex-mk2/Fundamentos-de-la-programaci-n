#Pregunta 3 adoptados (forma 2)
#Se debe crear una especie de menu con todos los animales (Gatos y perros)
#Que se ingresen al sistema

#Tecnicamente es un centro de adopcion para mascotas donde se tiene lo siguiente:
#Tipo de animal: perro o gato
#Estado vacuna: si o no
#Edad animal: entrada en meses
#Esterilizado: si o no
#Adoptado: si o no

#El programa dejará de ingresar elementos hasta que se ingrese la palabra fin

#Contadores
contarAnimales = 0
contarPerros = 0
contar_e_v = 0 #Contar solo si esta esterilizado y vacunado

#Sumas
sumaEdadesPerros = 0

#Obtener menor
menor = 101
registro_menor = 0

#Calculo del promedio
promedio = 0

#Logica del programa (Construccion general del problema v2)

#Ilegalisimo hacer esto pero meh
while True:
    especieAnimal = input("Ingrese una especie de animal (Perro o Gato) o Fin: ")
    if(especieAnimal == "Fin"):
        break

    elif(especieAnimal == "Gato" or especieAnimal == "Perro"):
         estadoVacunacion = input("Ingrese el estado de vacunacion (Si o No): ")
         edadAnimal = int(input("Ingrese la edad del animal en meses: "))
         esterilizado = input("¿Esta esterelizado? (Si o No): ")
         adoptado = input("¿Esta adoptado el animal? (Si o No): ")
         
         #Operacion para contar los animales a ingresar
         contarAnimales = contarAnimales + 1

         #Para saber si es perteneciente a la especie perro, se cuenta la cantidad y sumar sus edades
         if(especieAnimal == "Perro"):
             contarPerros = contarPerros + 1
             sumaEdadesPerros+= edadAnimal
         
         #Para saber si es adoptado, esterilizado y vacunado
         if(adoptado == "Si" and esterilizado == "Si" and estadoVacunacion == "Si"):
             contar_e_v = contar_e_v + 1

         #Para saber la especie mas joven que ha sido adoptada
         if(adoptado == "Si"):
             if(edadAnimal < menor): 
                 menor = edadAnimal 
                 registro_menor = especieAnimal
             elif(edadAnimal == menor):
                 menor = edadAnimal
                 registro_menor = especieAnimal
    else:
        print("No pertenece a las especies permitidas")

if(contarPerros > 0):
    promedio = (sumaEdadesPerros / contarPerros)
else:
    promedio = 0


print(f"La cantidad de animales ingresados son {contarAnimales}")
print(f"El promedio de las edades de los perros son {promedio}")
print(f"La cantidad de animales vacunados y esterilizados son {contar_e_v}")
print(f"El animal adoptado mas joven es de la especie {registro_menor} y tiene {menor} meses")

#promedio = (10 + 12)/2----->(2 perros)
#promedio = (22)/2
#promedio = 11

#Logica de and------> (O todos son verdadero)-------> condicion verdadera
#                     (1 todos son falso o uno de ellos es falso)-------> condicion falsa


#if(edadAnimal < menor): --------> "Si edadAnimal es menor a menor"
    #menor = edadAnimal  --------> "menor sera igual a edad animal"

#edadAnimal = 10 
#menor = 101

#(10 < 101)
#menor = 10

#Otro caso
#edadAnimal = 15
#menor = 10

#(15 < 10)
#menor = 10



#Logica de obtener el menor
#edadAnimal = 10
#menor = 10

#if(edadAnimal < menor): 
    #menor = edadAnimal

#edadAnimal = 5
#menor = 5
#(5 < 10)

#edadAnimal = 12
#menor = 5
#(12 < 5)