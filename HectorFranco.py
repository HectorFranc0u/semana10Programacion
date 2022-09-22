from cgitb import text
from msilib.schema import TextStyle
from platform import release
from tabnanny import check
import tkinter as tk
from tkinter import messagebox

def arietmetica():
    valor1 = caja1.get()
    valor2 = caja2.get()

    if x.get() == 1:
        resultado = float(valor1) + float(valor2)
        resultstr = str(resultado)
        messagebox.showinfo(title="resultado", message=resultstr)
    elif x.get() == 2:
        resultado = float(valor1) - float(valor2)
        resultstr = str(resultado)
        messagebox.showinfo(title="resultado", message=resultstr)
    elif x.get() == 3:
        resultado = float(valor1) * float(valor2)
        resultstr = str(resultado)
        messagebox.showinfo(title="resultado", message=resultstr)
    elif x.get() == 4:
        resultado = float(valor1) / float(valor2)
        resultstr = str(resultado)
        messagebox.showinfo(title="resultado", message=resultstr)
    else:
        messagebox.showinfo(title="resultado", message="creo que no entiendo muy bien lo que me pides")

ventana = tk.Tk()
x = tk.IntVar()
ventana.geometry("500x500")
caja1 = tk.Entry(ventana)
caja2 = tk.Entry(ventana)
btn1 = tk.Button(ventana, text="Calcular", height=5, width=5, command=arietmetica)
lb1 = tk.Label(ventana, text="Valor 1", width=5)
lb2 = tk.Label(ventana, text="Valor 2", width=5)
rb1 = tk.Radiobutton(ventana, text="Suma", value=1, variable=x)
rb2 = tk.Radiobutton(ventana, text="resta", value=2, variable=x)
rb3 = tk.Radiobutton(ventana, text="Multiplicacion", value=3, variable=x)
rb4 = tk.Radiobutton(ventana, text="Division", value=4, variable=x)

caja1.place(relx=0.1, rely=0.1, relwidth=0.3)
caja2.place(relx=0.1, rely=0.2, relwidth=0.3)
lb1.place(relx=0.5, rely=0.1)
lb2.place(relx=0.5, rely=0.2)
rb1.place(relx=0.1, rely=0.3)
rb2.place(relx=0.22, rely=0.3)
rb3.place(relx=0.32, rely=0.3)
rb4.place(relx=0.52, rely=0.3)
btn1.place(relx=0.1, rely=0.4, relwidth=0.5)

ventana.mainloop()