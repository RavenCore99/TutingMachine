def run(cadena):
    """
    EJERCICIO 4: Reconocer a^n b^n c^n
    Ejemplo: aaabbbccc
    """
    n = len(cadena) // 3
    if cadena == "a" * n + "b" * n + "c" * n and n > 0:
        return cadena, True
    return cadena, False
