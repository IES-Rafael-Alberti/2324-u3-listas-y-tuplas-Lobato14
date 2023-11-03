# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) 
# en dos listas y muestre por pantalla su producto escalar.

def productoEscalar(vector1, vector2):
    calculo = sum(vector1[indice] * vector2[indice] for indice in range(len(vector1)))
    return calculo

if __name__ == "__main__":
    # Entrada
    vector1 = [1, 2, 3]
    vector2 = [-1, 0, 2]
    # Proceso
    resultado = productoEscalar(vector1, vector2)
    # Salida
    print("El producto a escaler entre los vectores (1,2,3) y (-1,0,2) es", resultado)