import tkinter as tk
import random

# Opciones
PIEDRA = "piedra"
PAPEL = "papel"
TIJERA = "tijera"

# Imagenes
IMAGENES = {
    PIEDRA: "piedra.png",
    PAPEL: "papel.png",
    TIJERA: "tijera.png",
}

# Función para obtener la elección del jugador
def obtener_eleccion_jugador(opcion):
    global eleccion_jugador
    eleccion_jugador = opcion

# Función para generar la elección de la máquina
def generar_eleccion_maquina():
    return random.choice([PIEDRA, PAPEL, TIJERA])

# Función para determinar el ganador
def determinar_ganador(eleccion_jugador, eleccion_maquina):
    if eleccion_jugador == eleccion_maquina:
        return "Empate"
    elif eleccion_jugador == PIEDRA and eleccion_maquina == PAPEL:
        return "Máquina gana"
    elif eleccion_jugador == PIEDRA and eleccion_maquina == TIJERA:
        return "Jugador gana"
    elif eleccion_jugador == PAPEL and eleccion_maquina == PIEDRA:
        return "Jugador gana"
    elif eleccion_jugador == PAPEL and eleccion_maquina == TIJERA:
        return "Máquina gana"
    elif eleccion_jugador == TIJERA and eleccion_maquina == PIEDRA:
        return "Máquina gana"
    elif eleccion_jugador == TIJERA and eleccion_maquina == PAPEL:
        return "Jugador gana"

# Función para actualizar la interfaz
def actualizar_interfaz():
    # Mostrar la elección del jugador
    imagen_jugador.config(image=imagenes[eleccion_jugador])

    # Generar la elección de la máquina
    eleccion_maquina = generar_eleccion_maquina()

    # Mostrar la elección de la máquina
    imagen_maquina.config(image=imagenes[eleccion_maquina])

    # Mostrar el ganador
    resultado = determinar_ganador(eleccion_jugador, eleccion_maquina)
    etiqueta_resultado.config(text=resultado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel, Tijera")

# Crear las etiquetas
etiqueta_titulo = tk.Label(text="Piedra, Papel, Tijera")
etiqueta_jugador = tk.Label(text="Tu elección:")
etiqueta_maquina = tk.Label(text="Elección de la máquina:")
etiqueta_resultado = tk.Label(text="")

# Crear las imágenes
imagenes = {}
for opcion, nombre_imagen in IMAGENES.items():
    imagen = tk.PhotoImage(file=nombre_imagen)
    imagenes[opcion] = imagen

imagen_jugador = tk.Label(image=imagenes[PIEDRA])
imagen_maquina = tk.Label(image=imagenes[PIEDRA])

# Crear los botones
boton_piedra = tk.Button(text="Piedra", command=lambda: obtener_eleccion_jugador(PIEDRA))
boton_papel = tk.Button(text="Papel", command=lambda: obtener_eleccion_jugador(PAPEL))
boton_tijera = tk.Button(text="Tijera", command=lambda: obtener_eleccion_jugador(TIJERA))

# Posicionar los widgets
etiqueta_titulo.pack()
etiqueta_jugador.pack()
imagen_jugador.pack()
etiqueta_maquina.pack()
imagen_maquina.pack()
etiqueta_resultado.pack()
boton_piedra.pack()
boton_papel.pack()
boton_tijera.pack()

# Actualizar la interfaz por primera vez
actualizar_interfaz()

# Iniciar el bucle principal
ventana.mainloop()
