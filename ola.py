import random

salud = 100
piedras = 0


def obtener_piedra_vida(questPiedra):
    global piedras 
    loteria = questPiedra * random.randint(1, 100)
    print("Tu numero de la suerte es ", loteria)
    if loteria > 500 :
       piedras =+ 1
       print("Haz obtenido una piedra de vida")

    else :
      print("No has obtenido la piedra de vida")
      

while True:
    print("Elije tu suerte...")

    questPiedra = int(input("Selecciona un numero entre 1 y 20 "))

    if questPiedra < 21 :
        print("Ha elegido el numero ", questPiedra)
        break
    else :
        print("Opcion no válida")

obtener_piedra_vida(questPiedra)

print("Usted tiene ", piedras, " piedras de vida")



# Preguntar al usuario por su elección
while True:
    print("Elige un arma:")
    print("A. Espada")
    print("B. Hacha")

    # Leer la entrada del usuario
    opcion = input("Ingresa tu elección (Espada o Hacha): ")

    # Evaluar la elección del usuario
    if opcion.lower() == "espada":
        print("Has elegido la Espada.")
        break
    elif opcion.lower() == "hacha":
        print("Has elegido el Hacha.")
        break
    else:
        print("Opción no válida. Por favor, elige Espada o Hacha.")

print("Sus puntos de salud son: ", salud, " puntos")

print("Ha aparecido un duende")
print("El duende se ha equipado con una daga... Elige un numero del 1 al 10 para combatir")

#Comienzo del combate

dagaDuende = random.randint(1, 1000)


#funcion para batallas

def elegir_puntos_golpe():
     while True:
        opcion = int(input("Ingrese un número entre 1 y 10: "))
        if opcion < 11:
            return opcion
            break
        else:
            print("Por favor ingrese un número entre 1 y 10")


def calculadora_ataque(atackUser):
    print("Calculando su ataque...")
    ataque = atackUser * random.randint(1, 1000)
    print("Su ataque fue de ", ataque, " puntos de poder")
    return ataque


def batalla_normal(ataque):
        dagaDuende = 10
        if ataque > dagaDuende:
          print("¡Usted ha ganado el combate!")
        else:
          print("Usted pierde el combate")


elegir_puntos_golpe()
calculadora_ataque(atackUser)
batalla_normal(ataque)


if dagaDuende > 700 :
    salud= salud - 30
else :
    if dagaDuende > 400 and dagaDuende < 700 :
        salud = salud - 20
    if dagaDuende < 400 :
        salud = salud - 10

print("Usted queda con ", salud, " puntos de salud")





