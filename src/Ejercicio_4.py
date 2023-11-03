# Escribir un programa que pregunte al usuario los números ganadores 
# de la lotería primitiva, los almacene en una lista y los muestre por 
# pantalla ordenados de menor a mayor.

def ordenar_numeros(numeros_ganadores):
    numeros_lista = numeros_ganadores.split()
    for numero in numeros_lista:
        if not numero.isdigit():
            return "Error: Por favor, ingresa solo números separados por espacios."
    numeros_lista = [int(numero) for numero in numeros_lista]
    numeros_lista.sort()
    return numeros_lista

if __name__ == "__main__":
    # Entrada
    numeros_ganadores = input("Ingresa los números ganadores de la lotería primitiva separados por espacios: ")
    # Proceso
    while not numeros_ganadores.replace(" ", "").isdigit():
        print("Error: Por favor, ingresa solo números separados por espacios.")
        numeros_ganadores = input("Ingresa los números ganadores de la lotería primitiva separados por espacios: ")
    nums_ordenados = ordenar_numeros(numeros_ganadores)
    # Salida
    print("Números ganadores ordenados de menor a mayor:")
    print(nums_ordenados)
