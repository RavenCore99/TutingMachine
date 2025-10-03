from ejercicios import (
    ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5,
    ejercicio6, ejercicio7, ejercicio8, ejercicio9, ejercicio10
)

descripciones = {
    1: "Palíndromos binarios (ej: 1001, 11011)",
    2: "Complemento binario (ej: 1010 → 0101)",
    3: "Duplicar cadena unaria (ej: 111 → 111111)",
    4: "a^n b^n c^n (ej: aaabbbccc)",
    5: "Suma en unario (ej: 111+11 → 11111)",
    6: "Números binarios pares (ej: 110 es par)",
    7: "Copiar w#w (ej: 101# → 101#101)",
    8: "0^n1^n (ej: 0011, 000111)",
    9: "Incrementar binario (ej: 101 → 110)",
    10: "Detectar subcadena '101' (ej: 1101 contiene 101)",
}

ejercicios = {
    1: ejercicio1.run,
    2: ejercicio2.run,
    3: ejercicio3.run,
    4: ejercicio4.run,
    5: ejercicio5.run,
    6: ejercicio6.run,
    7: ejercicio7.run,
    8: ejercicio8.run,
    9: ejercicio9.run,
    10: ejercicio10.run,
}


def menu():
    print("\n=== SIMULADOR DE MÁQUINAS DE TURING ===")
    for i in range(1, 11):
        print(f"{i}. {descripciones[i]}")
    print("0. Salir")
    return int(input("Elige un ejercicio (0-10): "))


if _name_ == "_main_":
    while True:
        opcion = menu()
        if opcion == 0:
            print("👋 Adiós")
            break
        elif opcion in ejercicios:
            print("\n📌", descripciones[opcion])
            cadena = input("👉 Ingresa la cadena de prueba: ")
            resultado, aceptado = ejercicios[opcion](cadena)
            print("\nResultado:", resultado)
            print("Estado:", "✅ ACEPTADO" if aceptado else "❌ RECHAZADO")
        else:
            print("⚠ Opción inválida")