#Pregunta 3 adoptados (forma 1)
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

contar_v_e = 0
contarAnimales = 0
contarPerros = 0

#Lista para guardar los elementos
guardar_animales = []

#Suma edades de los perros
edadesPerros = 0

#Para obtener el promedio de las edades
promedio = 0

#Como se busca el mas joven de los animales
menor = 101
registrarAnimalJoven = 0

#Logica del programa (Contruccion a traves de listas v1)

while True:
    especieAnimal = input("Ingrese la especie de animal (Perro o Gato) o Fin: ")
    if(especieAnimal == "Fin"):
        break;
    elif (especieAnimal in ["Perro", "Gato"]):
         
         estadoVacunacion = input("Ingrese el estado de vacunacion (Si o No): ")
         edadAnimal = int(input("Ingrese la edad del animal en meses: "))
         esterilizado = input("¿Esta esterelizado? (Si o No): ")
         adoptado = input("¿Esta adoptado el animal? (Si o No): ")

         #Contar la cantidad de animales ingresados en el sistema
         contarAnimales = contarAnimales + 1

         guardar_animales.append(especieAnimal)
         guardar_animales.append(estadoVacunacion)
         guardar_animales.append(edadAnimal)
         guardar_animales.append(esterilizado)
         guardar_animales.append(adoptado)

         #Verificar si es perteneciente a la lista perro, contar cuantas veces y sumar sus edades
         if(especieAnimal == "Perro"):
             contarPerros = contarPerros + 1
             edadesPerros+= edadAnimal

         #Verificar si se cumple que esta adoptado, esta vacunado y esterilizado
         if(adoptado == "Si" and estadoVacunacion == "Si" and esterilizado == "Si"):
             contar_v_e = contar_v_e + 1

         #Verificar si se cumple que es adoptado y si su edad es menor    
         if(adoptado == "Si"):
             if(edadAnimal < menor):
                 menor = edadAnimal
                 registrarAnimalJoven = especieAnimal
             elif(edadAnimal == menor):
                 menor = edadAnimal
                 registrarAnimalJoven = especieAnimal
                 print("Aqui se registro un empate")
             
         
#Para calcular el promedio de las edades de los perros
if(contarPerros > 0):
    promedio = (edadesPerros / contarPerros)
else:
    promedio = 0

#Promedio = (todos los datos sumados / cantidad de datos)
#Analogia = (todas las notas de una asignatura / cantidad de evaluaciones de esa asignatura)


#Ahora se muestran todos los resultados
print(f"El total de animales ingresados son {contarAnimales}")
print(f"El promedio de las edades de los perros son {promedio}")
print(f"La cantidad de animales vacunados y esterilizados son {contar_v_e}")
print(f"El animal adoptado mas joven es de la especie {registrarAnimalJoven} y tiene {menor} meses")

