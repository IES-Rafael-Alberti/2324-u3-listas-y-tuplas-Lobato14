# Escribir un programa que pida al usuario una palabra y 
# muestre por pantalla el número de veces que contiene 
# cada vocal

def contar_vocales(palabra):
    vocales = "aeiou"
    conteo_vocales = {vocal: 0 for vocal in vocales}
    for letra in palabra.lower():
        if letra in vocales:
            conteo_vocales[letra] += 1
    return conteo_vocales

if __name__ == "__main__":
    # Entrada
    palabra = input("Ingrese una palabra: ")
    # Proceso
    while not palabra.isalpha():
        print("Por favor, ingrese una palabra sin números ni caracteres especiales.")
        palabra = input("Ingrese una palabra: ")
    resultado = contar_vocales(palabra)
    print("Número de veces que aparece cada vocal:")
    # Salida
    for vocal, conteo in resultado.items():
        print(f"{vocal}: {conteo}")