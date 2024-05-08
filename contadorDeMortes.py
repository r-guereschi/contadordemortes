import tkinter as tk
from pynput import keyboard

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")
        
        # Cor de fundo verde
        self.root.configure(bg="green")
        
        self.counter = 0
        
        # Cor do texto do contador como branco
        self.label = tk.Label(root, text=str(self.counter), font=("Helvetica", 24), fg="white", bg="green")
        self.label.pack(pady=20)

        # Configuração do listener de teclado
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
    def on_press(self, key):
        try:
            if key == keyboard.Key.enter:
                self.add_one()
            elif key == keyboard.Key.backspace:
                self.subtract_one()
            elif key == keyboard.Key.delete:
                self.reset_counter()
        except AttributeError:
            pass
        
    def add_one(self):
        self.counter += 1
        self.update_counter()

    def subtract_one(self):
        if self.counter > 0:
            self.counter -= 1
            self.update_counter()

    def reset_counter(self):
        self.counter = 0
        self.update_counter()
        
    def update_counter(self):
        self.label.config(text=str(self.counter))

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
