import tkinter as tk
import random

class AdivinaElNumeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Número")
        
        # Generar el número aleatorio
        self.numero_aleatorio = random.randint(1, 100)
        self.intentos = 0

        # Etiqueta de instrucciones
        self.label = tk.Label(root, text="Adivina un número entre 1 y 100", font=('Arial', 14))
        self.label.pack(pady=10)
        
        # Caja de entrada de número
        self.entrada = tk.Entry(root, font=('Arial', 14))
        self.entrada.pack(pady=10)
        
        # Botón para hacer el intento
        self.boton_adivinar = tk.Button(root, text="Adivinar", command=self.adivinar, font=('Arial', 14))
        self.boton_adivinar.pack(pady=10)
        
        # Etiqueta para mostrar el resultado
        self.resultado = tk.Label(root, text="", font=('Arial', 14))
        self.resultado.pack(pady=10)
    
    def adivinar(self):
        try:
            intento = int(self.entrada.get())
            self.intentos += 1

            if intento < self.numero_aleatorio:
                self.resultado.config(text="El número es mayor.")
            elif intento > self.numero_aleatorio:
                self.resultado.config(text="El número es menor.")
            else:
                self.resultado.config(text=f"¡Correcto! Lo adivinaste en {self.intentos} intentos.")
                self.boton_adivinar.config(state="disabled")
        except ValueError:
            self.resultado.config(text="Por favor, ingresa un número válido.")

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaElNumeroApp(root)
    root.mainloop()
