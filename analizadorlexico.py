#from ast import If
#from pprint import pp
#from typing import final
from genericpath import exists
from multiprocessing.reduction import duplicate
import re
import string
from unittest import result
from tokens import tokens
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import messagebox

#from Interfaz import datos
resultReservadas = []
resultCaracteresEspeciales = []
resultDelimitadores = []
resultIndefinidas = []
resultErrores = []

class analizador:
    tokens = tokens()
    def inicio_analizador(self, palabras):
        resultReservadas = []
        resultCaracteresEspeciales = []
        resultDelimitadores = []
        print("--- Lexico ---")
        for i in palabras:
            if(i in tokens.reservadas):
                resultReservadas.append(i)
                palabras.remove(i)
            if(i in tokens.caracteres_especiales):
                resultCaracteresEspeciales.append(i)
                palabras.remove(i)
            if(i in tokens.delimitadores):
                resultDelimitadores.append(i)
                palabras.remove(i)

            

        # for i in tokens.reservadas:
        #     for j in palabras:
        #         if (i == j):
        #             resultReservadas.append(i)
        #             palabras.remove(i)
        # for l in tokens.caracteres_especiales:
        #     for k in palabras:
        #         if (l == k):
        #             resultCaracteresEspeciales.append(k)
        #             palabras.remove(l)
        # for t in tokens.delimitadores:
        #     for f in palabras:
        #         if (t == f):
        #             resultDelimitadores.append(t)
        #             palabras.remove(t)

        for g in range (len(palabras)):
            dato = re.search("[a-zA-Z][a-zA-Z0-9_]*", palabras[g])
            if dato:
                resultIndefinidas.append(palabras[g])
            else:
                dato1 = re.search("^[0-9]+$", palabras[g])
                if dato1:
                    resultIndefinidas.append(palabras[g])
                else:
                    resultErrores.append(palabras[g])

        print("Token Reservadas: ",resultReservadas)
        print("Token Caracteres Especiales: ",resultCaracteresEspeciales)
        print("Token Delimitadores: ",resultDelimitadores)
        print("Token Indefinidas: ",resultIndefinidas)
        print("Errores: ",resultErrores)

    def funcAuxiliar(self, palabras):
        for i in tokens.reservadas:
            for j in palabras:
                if (i == j):
                    resultReservadas.append(i)
        
        for l in tokens.caracteres_especiales:
            for k in palabras:
                if (l == k):
                    resultCaracteresEspeciales.append(k)
        
        for t in tokens.delimitadores:
            for f in palabras:
                if (t == f):
                    resultDelimitadores.append(t)
        c = 0
        s = 0
        p = 0
        d = 0
        cs = 0
        i = 0
        pa = 0
        pc = 0
        dp = 0
        up = 0
        for cantidadReservadas in resultReservadas:
            if cantidadReservadas == "class":
                print("encontro un class")
                c += 1
            if cantidadReservadas == "self":
                print("encontro un self")
                s += 1
            if cantidadReservadas == "print":
                print("encontro un print")
                p += 1
            if cantidadReservadas == "def":
                print("encontro un def")
                d += 1
        for cantidadCaracteres in resultCaracteresEspeciales:
            if cantidadCaracteres == "'":
                print("encontro un ' ")
                cs += 1
        for cantidadDelimitadores in resultDelimitadores:
            if cantidadDelimitadores == "=":
                print("encontro un = ")
                i += 1
            if cantidadDelimitadores == "(":
                print("encontro un ( ")
                pa += 1
            if cantidadDelimitadores == ")":
                print("encontro un ) ")
                pc += 1
            if cantidadDelimitadores == ":":
                print("encontro un : ")
                dp += 1
            if cantidadDelimitadores == ".":
                print("encontro un . ")
                up += 1
        if c == 1 and s == 1 and p == 1 and d == 1 and cs == 2 and i == 2 and pa == 5 and pc == 5 and dp == 1 and up == 1:
            print("CUMPLE")
            palabras.remove("class")
            palabras.remove("self")
            palabras.remove("def")
            palabras.remove("print")
            palabras.remove("'")
            palabras.remove("'")
            palabras.remove("=")
            palabras.remove("=")
            palabras.remove("(")
            palabras.remove("(")
            palabras.remove("(")
            palabras.remove("(")
            palabras.remove("(")
            palabras.remove(")")
            palabras.remove(")")
            palabras.remove(")")
            palabras.remove(")")
            palabras.remove(")")
            palabras.remove(":")
            palabras.remove(".")
            
            print(palabras)
        else:
            print("NO CUMPLE")
