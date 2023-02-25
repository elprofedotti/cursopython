import tkinter as tk
from tkinter import ttk

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

window = tk.Tk()
opcion = tk.StringVar()
opcion.set(None)
radioNom1=tk.Radiobutton(window, text="Heloise", variable=opcion, 
            value='Heloise', command=seleccionar)
radioNom1.pack(anchor=tk.W)

radioNom2=tk.Radiobutton(window, text="Matias", variable=opcion, 
            value='Matias', command=seleccionar)
radioNom2.pack(anchor=tk.W)
radioNom3=tk.Radiobutton(window, text="Semilla", variable=opcion,
               value='Semilla', command=seleccionar)
radioNom3.pack(anchor=tk.W)
radioNom4=tk.Radiobutton(window, text="Micaela", variable=opcion,   
            value='Micaela', command=seleccionar)
radioNom4.pack(anchor=tk.W)

monitor = tk.Label(window)
monitor.pack()
btnBoton=tk.Button(window, text="Reiniciar", command=reset)
btnBoton.pack()

window.mainloop()