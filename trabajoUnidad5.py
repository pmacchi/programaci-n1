#Realizar la carga de dos nombres de personas distintos.

#Mostrar por pantalla luego ordenados en forma alfabética.

#print("Acomodador de nombres")

#opcion=input("Desea acomodar estos nombres? Y/N ")


#while opcion == "Y" :
#    nombre1=input("Ingrese su nombre aqui: ")
#    nombre2=input("Ingrese su nombre aqui: ")
#    if nombre1 > nombre2 :
#        print(nombre1 , nombre2)

#    else :
#        print(nombre2 , nombre1)

#    opcion=input("Desea acomodar dos nuevos nombres?")

#print("Gracias por usar nuestro programa")


# Cargar una oración por teclado. Mostrar luego cuantos espacios en
#blanco se ingresaron.
#Tené en cuenta que un espacio en blanco es igual a " ", en cambio una
#cadena vacía es ""

#oracion=input("Ingrese una oración")

#cantidadEspacios=0
#x=0

#while x < len(oracion) :
#    if oracion[x] == " " :
#        print("Espacio detectado")
#        cantidadEspacios= cantidadEspacios + 1
#    x = x + 1
        
#print("La cantidad de espacios es de: " , cantidadEspacios )


#| Ingresar una oración que puede tener letras tanto en mayúsculas como
#minúsculas.
#Contar la cantidad de vocales.
#Crear un segundo string con toda la oración en minúsculas para que sea
#más fácil disponer la condición que verifica que es una vocal.

selecion=input("Desea encontrar las vocales de una oracion? Y/N ")
seleccion=selecion.lower()

while seleccion == "y" :
    oracionX=input("Inserte oración aqui ")
    oracionI=oracionX.lower()

    oracion=0
    x=0
    while x < len(oracionI) :
            if oracionI[x] == "a" or oracionI[x] == "e" or oracionI[x] == "i" or oracionI[x] == "o" or oracionI[x] == "u" :
                print("Vocal encontrada")
                oracion= oracion + 1
            x = x + 1
    print("La oración ingresada es: " ,"'" , oracionI, "' y tiene " , oracion , " vocales.")
    seleccion=input("Desea encontrar nuevas vocales? Y/N ")
    
#| Solicitar el ingreso de una clave por teclado y almacenarla en una cadena
#de caracteres.
#Controlá que el string ingresado tenga entre 10 y 20 caracteres para que
#sea válido, en caso contrario mostrar un mensaje de error.

contraseña=input("Genere una contraseña entre 10 y 20 digitos")

while len(contraseña) >= 21 or len(contraseña) <= 10 :
    
    print("Contraseña Invalida Valida")
    contraseña=input("Por favor ingrese una contraseña válida")

print("Usted ha ingresado una contraseña válida")
    


    





