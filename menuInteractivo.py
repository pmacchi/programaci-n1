import random

print("#########MENU#########")

acceso=input("Desea acceder al menú? Y/N ")

while acceso == "Y" :
    print("1 - Menu")
    print("2 - Submenu")
    print("3 - Salir")
    opcion=int(input("Bienvido al menu, por favor ingrese una opción."))
    

    while opcion == 1 :
        print("&&& Juego de Adivinar Numero &&&")
        jugar=input("¿Quiere Jugar? Y/N ")
        while jugar == "Y" :
            nmr = random.randrange(10)
            numero = int(input("Elija un numero para jugar "))
            while numero != nmr :
                print("Intento fallido. Reintentar?")
                numero=int(input("Elija un nuevo numero para jugar "))
            print("Acertó!")
            jugar=input("Desea intentar de nuevo? ")
    acceso=input("Desea volver al menu anterior?")    

    while opcion == 2 :
        print("#########SubMENU#########")
        token=int(input("Generar TOKEN: "))
        while token < 4 and token > 10 :
            token=input("TOKEN no cumple requisitos minimos")
        print("TOKEN creado exitosamente")
        print("Su TOKEN es ", token )
        
    acceso=input("Desea volver al menu anterior?")    

    
    while opcion == 3 :  
               print("Gracias por usar nuestro menú")
               break

print("Apando programa")
