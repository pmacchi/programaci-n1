import tkinter as tk
import random

def iniciar_combate():
    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, "Hola Mundo\n")
    resultado_texto.insert(tk.END, "Buen día Guerrero! Era una noche calurosa cuando te cruzas con un enemigo conocido...\n")
    
    numero_inicial = int(entrada_numero.get())
    
    golpeInicial = (numero_inicial * random.randint(1, 10)) + random.randint(1, 50) - random.randint(1, 20)
    golpeGollum = (numero_inicial * random.randint(1, 10)) + random.randint(1, 50) - random.randint(1, 20)
    
    if golpeInicial > golpeGollum:
        resultado_texto.insert(tk.END, "Has ganado el combate\n")
    else:
        resultado_texto.insert(tk.END, "Tienes que defenderte... Toma un escudo\n")
        numero_nuevo = int(entrada_defensa.get())
        defensa = (numero_nuevo * random.randint(1, 10)) + random.randint(1, 50) - random.randint(1, 20)
        if defensa > golpeGollum:
            resultado_texto.insert(tk.END, "Has evadido con éxito\n")
        else:
            resultado_texto.insert(tk.END, "No has evadido\n")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Combate")
ventana.geometry("500x400")

# Crear widgets
etiqueta_numero = tk.Label(ventana, text="Ingresa un número:")
etiqueta_numero.pack()

entrada_numero = tk.Entry(ventana)
entrada_numero.pack()

etiqueta_defensa = tk.Label(ventana, text="Ingrese los puntos de defensa de su escudo:")
etiqueta_defensa.pack()

entrada_defensa = tk.Entry(ventana)
entrada_defensa.pack()

boton_comenzar = tk.Button(ventana, text="Comenzar Combate", command=iniciar_combate)
boton_comenzar.pack()

resultado_texto = tk.Text(ventana, height=10, width=50)
resultado_texto.pack()

# Mantener la ventana abierta
ventana.mainloop()
