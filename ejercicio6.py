def run(cadena):
    """
    EJERCICIO 6: Reconocer números binarios pares
    Acepta si termina en 0
    """
    if not set(cadena).issubset({"0", "1"}):
        return cadena, False
    return cadena, cadena.endswith("0")