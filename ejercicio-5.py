def run(cadena):
    """
    EJERCICIO 5: Suma en unario
    Ejemplo: 111+11 → 11111
    """
    if "+" not in cadena:
        return cadena, False
    partes = cadena.split("+")
    if not all(set(p).issubset({"1"}) for p in partes):
        return cadena, False
    resultado = "1" * (len(partes[0]) + len(partes[1]))
    return resultado, True
