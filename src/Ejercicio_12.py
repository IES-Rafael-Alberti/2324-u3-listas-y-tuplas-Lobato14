# Escribir un programa que almacene las matrices A=(123456) y B=(−100111) 
# en una lista y muestre por pantalla su producto. Nota: Para representar 
# matrices mediante listas usar listas anidadas, representando cada vector 
# fila en una lista.

def multiplicar_matrices(matriz_a, matriz_b):
    resultado = []
    for fila_matriz_a in range(len(matriz_a)):
        fila_resultado = []
        for columna_matriz_b in range(len(matriz_b[0])):
            suma = 0
            for elemento in range(len(matriz_b)):
                suma += matriz_a[fila_matriz_a][elemento] * matriz_b[elemento][columna_matriz_b]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

if __name__ == "__main__":
    # Entrada
    matriz_A = [[1, 2, 3, 4, 5, 6]]
    matriz_B = [[-1, 0, 0, 1, 1, 1]]
    # Proceso
    matriz_resultado = multiplicar_matrices(matriz_A, matriz_B)
    # Salida
    print("El resultado es ", matriz_resultado)