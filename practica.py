from cgitb import text
from dis import code_info
from email import message
from logging.config import valid_ident
import tkinter as tk
from tkinter import messagebox
#from tkinter import*

def ejemplo():
    #exto[text]= "Hola Mundo"
    variable = caja[text]
    messagebox.showinfo(message=variable)

ventana = tk.Tk()
ventana.geometry("500x500")
button = tk.Button(ventana, text= "Boton",height=5, width=5, bg="Blue", command=ejemplo)
caja = tk.Entry(ventana)
caja2 = tk.Entry(ventana)
texto = tk.Label(ventana, text="Esto es un label")
texto2 = tk.Label(ventana, text="Esto es un label2")
op = tk.Radiobutton(ventana, text="opcion 1", value=1)
op2 = tk.Radiobutton(ventana, text="opcion 2", value=2)
op3 = tk.Radiobutton(ventana, text="opcion 3", value=3)

# Posicion relativa
#caja.place(relx=0.2,rely=0.2, relwidth=0.5)

#metodo grid :v 
caja.grid(row=0,column=0)
texto.grid(row=0, column=1)

caja2.grid(row=1,column=0)
texto2.grid(row=1,column=1)
button.grid(row=3,column=4)

"""

metodo place
caja.place(x=20, y=10, width=100)
texto.place(x=170, y=10, width=100)
caja2.place(x=20, y=50, width=100)
texto2.place(x=170, y=50, width=100)
button.place(x=170, y=80, height=30, width=100)
op.place(x=50, y=100, height=50,width=50)
op2.place(x=150,y=150,height=50, width=100)
"""
ventana.mainloop()
