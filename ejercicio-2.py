def run(cadena):
    """
    EJERCICIO 2: Complemento binario
    Cambia 0->1 y 1->0
    """
    if not set(cadena).issubset({"0", "1"}):
        return cadena, False
    resultado = "".join("1" if c == "0" else "0" for c in cadena)
    return resultado, True
