#-----------------------
     #----------------------



def run(cadena):
    """
    EJERCICIO 7: Copiar cadena w#w
    Ejemplo: 101# → 101#101
    """
    if "#" not in cadena:
        return cadena, False
    w = cadena.split("#")[0]
    return w + "#" + w, True