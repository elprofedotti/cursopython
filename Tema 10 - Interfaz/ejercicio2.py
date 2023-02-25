import tkinter as tk


window = tk.Tk()
#elemento = tk.StringVar()
listbox = tk.Listbox(window)
for item in ["Heloise", "Matias", "Semilla", "Madhav", "Micaela"]:
    listbox.insert(tk.END, item)
listbox.pack()
label=tk.Label(text="Lista de nombres de personas hermosas")
label.pack()
window.mainloop()