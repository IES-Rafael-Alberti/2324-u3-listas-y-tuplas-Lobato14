# Escribir un programa que pida al usuario una palabra y muestre por pantalla 
# si es un palíndromo.

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    while not palabra.isalpha() or ' ' in palabra:
        print("Por favor, ingrese una palabra sin números y sin espacios.")
        palabra = input("Ingrese una palabra: ")

    if es_palindromo(palabra):
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")