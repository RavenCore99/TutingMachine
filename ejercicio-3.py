def run(cadena):
    """
    EJERCICIO 3: Duplicar cadena unaria
    Duplica la cantidad de 1s
    Ejemplo: 111 → 111111
    """
    if not set(cadena).issubset({"1"}):
        return cadena, False
    return cadena * 2, True
