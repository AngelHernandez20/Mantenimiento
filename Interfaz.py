from cProfile import label
from email.mime import image
from enum import auto
from lib2to3.pgen2 import token
from tkinter import *    
from tkinter import ttk
from tkinter import messagebox


from click import command
#from typing_extensions import Self
#from analizadorlexico import analizador
#from analizador_L import analiza
import re
#from tkinter import PhotoImage
from analizadorlexico import *
raiz = Tk()

a = analizador()

def datos():
  print(entrada.get())
  palabras = re.split("\s",entrada.get()) # se divide las palabras por cada espacio que encuentra
  #newList = palabras.copy()
  # caja.insert(0,"Reservadas: ", resultReservadas)
  # print("Aqui deberia mostrarse", resultReservadas)
  a.inicio_analizador(palabras)

entrada = StringVar()
#entrada2 = StringVar()
# tamaño ventana
#raiz.resizable(False,False)
raiz.geometry('1050x500') 
# color fondo
raiz.configure(bg = 'beige')
# titulo 
raiz.title('Lenguajes y Automatas')
#label.place(x=30,y=60)
#caja.place(x=70,y=150)
#imagen = PhotoImage(file = "Captura.png")
#background = Label(image = imagen)
#background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
caja = Entry(raiz,textvariable=entrada)
#caja = Entry(raiz,textvariable=entrada2).pack()
caja.place(x=278,y=57, width="500", height="35")
ttk.Button(raiz, text='Busqueda', command=datos).place(x=500,y=30, width="100",height="24")
#ttk.Button(raiz, text='Busqueda', command=datos).pack()

ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)

listbox= Listbox()
listbox.place(relx=0.25, rely=0.20, relheight=0.7, relwidth=0.5 )






raiz.mainloop()