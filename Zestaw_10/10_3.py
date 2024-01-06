import tkinter as tk
import random

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")
        self.credits = 1000
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(pady=20)

        self.symbols = [[tk.Label(self.game_frame, text="0", font=("Helvetica", 24), width=4, height=2) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.symbols[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.spin_button = tk.Button(self.root, text="Spin", command=self.spin)
        self.spin_button.pack(pady=10)

        self.credits_label = tk.Label(self.root, text=f"Credits: {self.credits}", font=("Helvetica", 16))
        self.credits_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.pack()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        game_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="Start Game", command=self.spin)
        game_menu.add_command(label="Add Credits", command=self.add_credits)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.root.quit)

    def spin(self):
        if self.credits > 0:
            self.credits -= 10
            symbols = [random.randint(1, 5) for _ in range(9)]
            index = 0
            for i in range(3):
                for j in range(3):
                    self.symbols[i][j].config(text=symbols[index])
                    index += 1
            
            self.check_win(symbols)
            self.credits_label.config(text=f"Credits: {self.credits}")
        else:
            self.result_label.config(text="Not enough credits!")

    def add_credits(self):
        self.credits += 50
        self.credits_label.config(text=f"Credits: {self.credits}")

    def check_win(self, symbols):
        if symbols[0] == symbols[1] == symbols[2]:
            self.credits += 30
            self.result_label.config(text="You won 30 credits!")
        else:
            self.result_label.config(text="No win this time.")

root = tk.Tk()
app = SlotMachine(root)
root.mainloop()
