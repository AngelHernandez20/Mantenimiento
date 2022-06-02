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
#resultReservadas = []
#resultCaracteresEspeciales = []
#resultDelimitadores = []



class analizador:
    tokens = tokens()
    def inicio_analizador(self, palabras):
        resultReservadas = []
        resultCaracteresEspeciales = []
        resultDelimitadores = []
        resultIndefinidas = []
        resultErrores = []
        resultDigitos = []
        listResultados = []
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
        listResultados.append(resultReservadas)
        listResultados.append(resultCaracteresEspeciales)
        listResultados.append(resultDelimitadores)
        listResultados.append(resultIndefinidas)
        listResultados.append(resultDigitos)
        listResultados.append(resultErrores)
        return listResultados

    