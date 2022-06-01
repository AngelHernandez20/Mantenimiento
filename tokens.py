import numpy as np


class tokens:

    reservadas = np.array(["def","self","print","class"])
    caracteres_especiales = np.array(["'"])
    delimitadores = np.array(["=", "(", ")", ":", "."])
    #indefinidas = ["[a-zA-Z][a-zA-Z0-9_]*"]

    #listTokens = []

    #listTokens.append(reservadas)
    #listTokens.append(caracteres_especiales)
    #listTokens.append(delimitadores)
    #listTokens.append(indefinidas)
