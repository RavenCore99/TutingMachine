def run(cadena):
    """
    EJERCICIO 8: Reconocer 0^n1^n
    Ejemplo: 0011, 000111
    """
    n = len(cadena) // 2
    if cadena == "0" * n + "1" * n and n > 0:
        return cadena, True
    return cadena, False

#----------------------------- 
#---------------
