from cProfile import label
from email.mime import image
from enum import auto
from lib2to3.pgen2 import token
from tkinter import *    
from tkinter import ttk
from tkinter import messagebox
import re
from turtle import color

from numpy import place
from analizadorlexico import *
raiz = Tk()

a = analizador()


def enviardatos():
  listbox.delete(0, END)
  print(entrada.get())
  palabras = re.split("\s",entrada.get())
  bandera = a.inicio_analizador(palabras)
  mostrar(bandera)
  #a.inicio_analizador(palabras)
  

def mostrar(bandera):
  print("MOSTRAR DATOS")
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
raiz.configure(bg = 'lightblue')
raiz.title('Lenguajes y Automatas')
caja = Entry(raiz,textvariable=entrada)
caja.place(x=278,y=70, width="500", height="35")
caja.configure(bg='white')  
ttk.Button(raiz, text='Busqueda', command=enviardatos).place(x=500,y=43, width="100",height="24")
ttk.Button(raiz, text='Reiniciar',command=reiniciar).place(x=800,y=250)
ttk.Button(raiz, text='Salir', command=quit).place(x=525,y=465, width="50",height="25")
listbox= Listbox()
listbox.place(relx=0.25, rely=0.22, relheight=0.7, relwidth=0.5 )

labelExample = Label(raiz, text="Analizador Lexico de una Clase en Python")
labelExample.place(x=430, y=10, width="250",height="24" )


raiz.mainloop()