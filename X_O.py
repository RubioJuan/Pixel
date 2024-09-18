import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Variables del juego
        self.turn = "X"
        self.board = [[None] * 3 for _ in range(3)]

        # Crear botones de la cuadrícula
        self.buttons = [[None] * 3 for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(root, text="", font=("Arial", 40), width=5, height=2, command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

        # Botón para reiniciar el juego
        self.reset_button = tk.Button(root, text="Reiniciar", font=("Arial", 16), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    def on_click(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)
            if self.check_winner(self.turn):
                messagebox.showinfo("Tic Tac Toe", f"¡El jugador {self.turn} gana!")
                self.reset_game()
            elif all(cell is not None for row in self.board for cell in row):
                messagebox.showinfo("Tic Tac Toe", "¡Es un empate!")
                self.reset_game()
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self, player):
        # Chequeo de filas, columnas y diagonales
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def reset_game(self):
        self.turn = "X"
        self.board = [[None] * 3 for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()