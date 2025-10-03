def run(cadena):
    """
    EJERCICIO 9: Incrementar número binario
    Ejemplo: 101 → 110
    """
    try:
        numero = int(cadena, 2)
        return bin(numero + 1)[2:], True
    except:
        return cadena, False