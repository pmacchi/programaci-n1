import random

#var=1

#while var<11 :
#    print(var)
#    var+=1

#suma=0
#cont=1

#while cont < 50 :
#    suma= suma + cont
#   cont+=1

#print(suma)


#IMPRIMIR NUMEROS PARES

#numeroPar=1

#while numeroPar <= 20 :
#    if numeroPar % 2 == 0 :
#        print(numeroPar)
#    numeroPar = numeroPar + 1
    

#TABLA DE MULTIPLICAR

#numero=int(input("Ingrese un numero"))

#contador=1

#while contador < 11 :
#    print(numero, " x ", contador, " = ", contador*numero)
#    contador+= 1

#CONTADOR DE VOCALES


#var1= input("Ingrese una linea o enter para terminar: ")
#var2= input("Ingrese una linea o enter para terminar: ")
#var3= input("Ingrese una linea o enter para terminar: ")

#print("******************")
#print("*     ", var1, "     *")
#print("*     ", var2, "     *")
#print("*     ", var3, "     *")
#print("******************")


#producto=input("Ingrese un producto")

rta = input("Desea Calcular su Promedio? Y/N ")


while rta == "Y" :
      nota1 = int(input("Ingrese primer nota "))
      nota2 = int(input("Ingrese primer nota "))
      nota3 = int(input("Ingrese primer nota "))
      promedio=(nota1+nota2+nota3)/3
      print(promedio)
      rta = input("Desea calcular otro promedio? ")


numpar = int(input("Ingrese un numero"))

contador = 0

while contador <= numpar :
      if contador % 2 == 0 :
            print(contador)
      contador = contador + 1
            


print("######################### JUEGO###############################")
print("###################ADIVINA EL NUMERO##########################")

numeroRnd=random.randrange(10)

usuarioValor=int(input("Ingrese un numero para jugar: "))

while usuarioValor != numeroRnd :
      print("Ha elegido un número incorrecto. Por favor intente nuevamente")
      usuarioValor=int(input("Ingrese su nueva opción aqui"))

print("Ha acertado")


      
