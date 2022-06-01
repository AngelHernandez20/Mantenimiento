from cProfile import label
from email.mime import image
from enum import auto
from lib2to3.pgen2 import token
from tkinter import *    
from tkinter import ttk
from tkinter import messagebox
import re
from analizadorlexico import *
raiz = Tk()

a = analizador()


def datos():
  #listbox.delete(0, END)
  print(entrada.get())
  palabras = re.split("\s",entrada.get())
  #a.inicio_analizador(palabras)
  bandera = a.inicio_analizador(palabras)
  print(bandera)
  items = (
    "-- Reservadas --",
    bandera[0],
    " ",
    "-- Caracteres especiales --",
    bandera[1],
    " ",
    "-- Delimitadores --",
    bandera[2],
    " ",
    "-- Indefinidas --",
    bandera[3],
    " ",
    "-- Digitos --",
    bandera[4],
    "  ",
    "-- Errores --",
    bandera[5]
  )
  listbox.insert(0, *items)

  
def reiniciar():
  print("REINICIO") 
  caja.delete(0, END)
  listbox.delete(0, END)

entrada = StringVar()
raiz.geometry('1050x500') 
raiz.configure(bg = 'beige')
raiz.title('Lenguajes y Automatas')
caja = Entry(raiz,textvariable=entrada)
caja.place(x=278,y=57, width="500", height="35")
ttk.Button(raiz, text='Busqueda', command=datos).place(x=500,y=30, width="100",height="24")
ttk.Button(raiz, text='Reiniciar',command=reiniciar).place(x=800,y=250)
ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
listbox= Listbox()
listbox.place(relx=0.25, rely=0.20, relheight=0.7, relwidth=0.5 )

raiz.mainloop()