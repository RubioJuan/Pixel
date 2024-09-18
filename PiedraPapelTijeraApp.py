import tkinter as tk
from tkinter import messagebox
import random

class PiedraPapelTijeraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")
        
        # Puntuaciones
        self.puntuacion_jugador = 0
        self.puntuacion_computadora = 0
        
        # Etiquetas de puntuación
        self.label_puntuacion = tk.Label(root, text=f"Jugador: {self.puntuacion_jugador}  Computadora: {self.puntuacion_computadora}", font=('Arial', 16))
        self.label_puntuacion.pack(pady=20)

        # Etiqueta de instrucciones
        self.label_instrucciones = tk.Label(root, text="Elige tu jugada", font=('Arial', 14))
        self.label_instrucciones.pack(pady=10)

        # Botones de las opciones
        self.boton_piedra = tk.Button(root, text="Piedra", command=lambda: self.jugar("Piedra"), width=15, font=('Arial', 12))
        self.boton_piedra.pack(pady=5)

        self.boton_papel = tk.Button(root, text="Papel", command=lambda: self.jugar("Papel"), width=15, font=('Arial', 12))
        self.boton_papel.pack(pady=5)

        self.boton_tijera = tk.Button(root, text="Tijera", command=lambda: self.jugar("Tijera"), width=15, font=('Arial', 12))
        self.boton_tijera.pack(pady=5)

        # Etiqueta para mostrar el resultado de cada ronda
        self.label_resultado = tk.Label(root, text="", font=('Arial', 14))
        self.label_resultado.pack(pady=10)

    def jugar(self, eleccion_jugador):
        eleccion_computadora = random.choice(["Piedra", "Papel", "Tijera"])
        resultado = self.determinar_ganador(eleccion_jugador, eleccion_computadora)

        if resultado == "Empate":
            self.label_resultado.config(text=f"Empate! Ambos eligieron {eleccion_jugador}.")
        elif resultado == "Jugador":
            self.puntuacion_jugador += 1
            self.label_resultado.config(text=f"Ganaste! {eleccion_jugador} vence a {eleccion_computadora}.")
        else:
            self.puntuacion_computadora += 1
            self.label_resultado.config(text=f"Perdiste! {eleccion_computadora} vence a {eleccion_jugador}.")

        # Actualizar la puntuación
        self.label_puntuacion.config(text=f"Jugador: {self.puntuacion_jugador}  Computadora: {self.puntuacion_computadora}")

        # Verificar si alguien ha ganado
        self.verificar_ganador()

    def determinar_ganador(self, jugador, computadora):
        if jugador == computadora:
            return "Empate"
        elif (jugador == "Piedra" and computadora == "Tijera") or \
             (jugador == "Papel" and computadora == "Piedra") or \
             (jugador == "Tijera" and computadora == "Papel"):
            return "Jugador"
        else:
            return "Computadora"
    
    def verificar_ganador(self):
        if self.puntuacion_jugador == 5:
            messagebox.showinfo("Piedra, Papel o Tijera", "¡Felicidades, has ganado el juego!")
            self.reiniciar_juego()
        elif self.puntuacion_computadora == 5:
            messagebox.showinfo("Piedra, Papel o Tijera", "La computadora ha ganado el juego. ¡Mejor suerte la próxima vez!")
            self.reiniciar_juego()

    def reiniciar_juego(self):
        # Reiniciar las puntuaciones
        self.puntuacion_jugador = 0
        self.puntuacion_computadora = 0
        self.label_puntuacion.config(text=f"Jugador: {self.puntuacion_jugador}  Computadora: {self.puntuacion_computadora}")
        self.label_resultado.config(text="")

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = PiedraPapelTijeraApp(root)
    root.mainloop()