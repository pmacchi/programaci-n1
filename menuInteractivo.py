import random

print("#########MENU#########")

acceso=input("Desea acceder al menú? Y/N ").upper()

while acceso == "Y" :
    print("1 - Menu")
    print("2 - Submenu")
    print("3 - Mail")
    print("4 - Salir")
    opcion=int(input("Bienvido al menu, por favor ingrese una opción."))
    

    if opcion == 1 :
        print("&&& Juego de Adivinar Numero &&&")
        jugar=input("¿Quiere Jugar? Y/N ").upper()
        while jugar == "Y" :
            nmr = random.randrange(10)
            numero = int(input("Elija un numero para jugar "))
            while numero != nmr :
                print("Intento fallido. Reintentar?")
                numero=int(input("Elija un nuevo numero para jugar "))
            print("Acertó!")
            jugar=input("Desea volver a jugar?")
            

    elif opcion == 2 :
        print("#########SubMENU#########")
        token=int(input("Generar TOKEN: "))
        while token < 4 and token > 10 :
            token=input("TOKEN no cumple requisitos minimos")
        print("TOKEN creado exitosamente")
        print("Su TOKEN es ", token )

    elif opcion == 3 :
        print("######################")
        print("#########MAIL#########")
        print("######################")

        #while opcion == 3 :
        mail=input("Ingrese su mail aqui")         
        cantidad=0
        x=0
        while x < len(mail) :
            if mail[x]=="@" :
                cantidad = cantidad + 1
            x = x + 1
        if cantidad == 1 :
                print("Usted ingresó un email válido")
                    
        elif cantidad == 0 :
                print("Mail incorrecto!")
                mail=input("Ingrese")

                
             
    elif opcion == 4 :  
               print("Gracias por usar nuestro menú")
               

    acceso=input("Desea acceder al menú? Y/N ").upper()

print("Apagando programa")
