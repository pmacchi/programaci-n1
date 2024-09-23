print("Bienvenido a nuestro programa")
nombre=input("Ingrese su nombre ")
materia=input("De que materia quisiera averiguar su promedio? ")

print("Bienvenido ", nombre, " vamos a calcular tu promedio de ", materia, " de este año")

cantidadNotas = int(input("Cuantas notas desea cargar? "))
print("Usted cargará", cantidadNotas, "notas")

val = input("Desea calcular su promedio? S/N ")

while val == "s":
    x = 1
    acumuladorNotas = 0
    
    while x <= cantidadNotas:
        nota = int(input("Ingrese una nota: "))
        print("Usted ingresó: ", nota)
        acumuladorNotas = acumuladorNotas + nota
        x = x + 1
    
    promedio = acumuladorNotas // cantidadNotas
    print("La suma de los", cantidadNotas, "valores es", acumuladorNotas)
    print("Su promedio es", promedio)
    
    val = input("Desea calcular otro promedio? S/N ")


print("Calculando su ranking...")
if promedio == 10 :
    print("Felicidades, su desempeño fue sobresaliente")

else :

    if promedio >=4 and promedio <= 7 :
        print("Regular")

    if promedio >=7 and promedio < 10 :
        print("Aprobado")

    else :
         print("Desaprobado")
              
print("Gracias por utilizar este programa")
