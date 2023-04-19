import tkinter as tk
import sqlite3

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Mi aplicación")

        self.label_mercancia = tk.Label(master, text="Mercancia:")
        self.label_mercancia.grid(row=0, column=0, padx=5, pady=5)

        self.entry_mercancia = tk.Entry(master, width=30)
        self.entry_mercancia.grid(row=0, column=1, padx=5, pady=5)

        self.label_pais = tk.Label(master, text="País:")
        self.label_pais.grid(row=1, column=0, padx=5, pady=5)

        self.entry_pais = tk.Entry(master, width=30)
        self.entry_pais.grid(row=1, column=1, padx=5, pady=5)

        self.button_guardar = tk.Button(master, text="Guardar", command=self.guardar_datos)
        self.button_guardar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        
        
        
        
        
        
        
        
        
        
        

    def guardar_datos(self):
        # Obtiene los valores de los campos de entrada
        mercancia = self.entry_mercancia.get()
        pais = self.entry_pais.get()

        # Conecta con la base de datos
        conn = sqlite3.connect("C:/Users/12103/Documents/GitHub/TercerPa/POO EXAMEN 3ER PARCIAL/Importaciones.db")
        c = conn.cursor()

        # Inserta los datos en la tabla TB_Europa
        c.execute("INSERT INTO TB_Europa (Mercancia, Pais) VALUES (?, ?)", (mercancia, pais))

        # Guarda los cambios en la base de datos y cierra la conexión
        conn.commit()
        conn.close()

        # Limpia los campos de entrada
        self.entry_mercancia.delete(0, tk.END)
        self.entry_pais.delete(0, tk.END)

root = tk.Tk()
app = App(root)
root.mainloop()