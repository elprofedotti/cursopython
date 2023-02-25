import tkinter as tk
from tkinter import ttk


window=tkinter.Tk()
#geometria pack
label_hola = tkinter.Label(window, text="hola", bg="yellow", fg="blue")
label_hola.pack(ipadx=50, ipady=50, fill="x", side="left", expand="True")

label_adios = tkinter.Label(window, text="hola", bg="red", fg="white")
label_adios.pack(ipadx=50, ipady=100,fill="y", side="right")

window2=tkinter.Tk()
#geometira grid -->filas columnas
#(0,0)(0,1)(0,2)
#label entry

#(1,0)(1,1)(1,2)
#label entry

#(2,0)(2,1)(2,2)
window2.columnconfigure(0, weight=1)
window2.columnconfigure(1, weight=3)

usuarioLabel=ttk.Label(window2, text="Usuario: ")
usuarioLabel.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
usuarioEntry=ttk.Entry(window2)
usuarioEntry.grid(column=2, row=0, sticky=tkinter.E, padx=5, pady=5)

passLabel=ttk.Label(window2, text="Password: ")
passLabel.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)
passEntry=ttk.Entry(window2, show="*")
passEntry.grid(column=2, row=1, sticky=tkinter.E, padx=5, pady=5)

btnBoton=ttk.Button(window2, text="Login")
btnBoton.grid(column=1, row=2, sticky=tkinter.E, padx=5, pady=5)


#posisionamiento absoluto indicamos las x e y
window3=tkinter.Tk()
label = tkinter.Label(window3, text="hola", bg="yellow", fg="blue")
label.place(x=10, y=15)

window.mainloop()
window2.mainloop()
window3.mainloop()