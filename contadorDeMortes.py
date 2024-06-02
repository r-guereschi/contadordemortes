import tkinter as tk
from tkinter import simpledialog, messagebox
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
        self.add_key = keyboard.Key.enter
        self.sub_key = keyboard.Key.backspace
        self.reset_key = keyboard.Key.delete
        
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
        # Criação do menu
        self.create_menu()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Configurações", menu=settings_menu)
        settings_menu.add_command(label="Mudar Teclas de Atalho", command=self.change_shortcuts)
    
    def change_shortcuts(self):
        self.add_key = self.get_key("Adicionar")
        self.sub_key = self.get_key("Subtrair")
        self.reset_key = self.get_key("Resetar")
        messagebox.showinfo("Informação", "Teclas de atalho atualizadas com sucesso!")
        
    def get_key(self, action):
        messagebox.showinfo("Informação", f"Pressione a nova tecla para {action}")
        with keyboard.Listener(on_press=self.capture_key) as listener:
            listener.join()
        return self.captured_key

    def capture_key(self, key):
        self.captured_key = key
        return False  # Para parar o listener após a captura da tecla
    
    def on_press(self, key):
        try:
            if key == self.add_key:
                self.add_one()
            elif key == self.sub_key:
                self.subtract_one()
            elif key == self.reset_key:
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
