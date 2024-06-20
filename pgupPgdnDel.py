import tkinter as tk
from tkinter import font, colorchooser, simpledialog, messagebox
from pynput import keyboard
import json
import os

CONFIG_FILE = "config.json"

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")
        
        # Definindo o tamanho inicial da janela
        self.root.geometry("300x200")  # Largura x Altura
        
        # Cor de fundo verde
        self.root.configure(bg="green")
        
        # Carregar configurações
        self.config = self.load_config()
        
        self.counter = self.config.get("counter", 0)
        self.font_family = self.config.get("font_family", "Helvetica")
        self.font_size = self.config.get("font_size", 24)
        self.font_color = self.config.get("font_color", "white")
        self.counter_text = self.config.get("counter_text", "Contador")
        
        # Cor do texto do contador como branco
        self.label = tk.Label(root, text=self.get_counter_label_text(), font=(self.font_family, self.font_size), fg=self.font_color, bg="green")
        self.label.pack(pady=20)

        # Configuração do listener de teclado
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
        # Criação do menu
        self.create_menu()
    
    def get_counter_label_text(self):
        return f"{self.counter_text}: {self.counter}"
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Configurações", menu=settings_menu)
        settings_menu.add_command(label="Escolher Fonte", command=self.choose_font)
        settings_menu.add_command(label="Escolher Tamanho da Fonte", command=self.choose_font_size)
        settings_menu.add_command(label="Escolher Cor da Fonte", command=self.choose_font_color)
        settings_menu.add_separator()
        settings_menu.add_command(label="Escolher Texto do Contador", command=self.choose_counter_text)
    
    def choose_font(self):
        font_chooser = tk.Toplevel(self.root)
        font_chooser.title("Escolher Fonte")
        
        tk.Label(font_chooser, text="Família da Fonte:").pack()
        self.font_family_var = tk.StringVar(value=self.font_family)
        family_menu = tk.OptionMenu(font_chooser, self.font_family_var, *font.families())
        family_menu.pack()
        
        def apply_font():
            self.font_family = self.font_family_var.get()
            self.update_counter()
            font_chooser.destroy()
        
        tk.Button(font_chooser, text="OK", command=apply_font).pack()
    
    def choose_font_size(self):
        size = simpledialog.askinteger("Tamanho da Fonte", "Digite o tamanho da fonte:", initialvalue=self.font_size)
        if size:
            self.font_size = size
            self.update_counter()
    
    def choose_font_color(self):
        color = colorchooser.askcolor(title="Escolher Cor da Fonte")[1]
        if color:
            self.font_color = color
            self.update_counter()
    
    def choose_counter_text(self):
        text = simpledialog.askstring("Texto do Contador", "Digite o texto desejado para o contador:", initialvalue=self.counter_text)
        if text:
            self.counter_text = text
            self.update_counter()
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.page_up:
                self.add_one()
            elif key == keyboard.Key.page_down:
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
        self.label.config(text=self.get_counter_label_text(), font=(self.font_family, self.font_size), fg=self.font_color)
        self.save_config()
        
    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as file:
                return json.load(file)
        return {}
    
    def save_config(self):
        config = {
            "counter": self.counter,
            "font_family": self.font_family,
            "font_size": self.font_size,
            "font_color": self.font_color,
            "counter_text": self.counter_text
        }
        with open(CONFIG_FILE, 'w') as file:
            json.dump(config, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
