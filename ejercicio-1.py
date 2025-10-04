def run(cadena):
    """
    EJERCICIO 1: Reconocer palíndromos binarios
    Acepta si la cadena es igual al revés.
    """
    return cadena, (cadena == cadena[::-1])
