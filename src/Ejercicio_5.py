# Escribir un programa que almacene en una lista los números del 1 al 10 y 
# los muestre por pantalla en orden inverso separados por comas.

def anadirListaNum(listaNumeros):
    for numero in range(1, 11):
        listaNumeros.append(numero)
    return listaNumeros.reverse()
    
if __name__ == "__main__":
    # Entrada
    listaNumeros = []
    # Proceso
    anadirListaNum(listaNumeros)
    # Convierte los números a cadena y los une con comas
    numeros_invertidos = ", ".join(str(num) for num in listaNumeros)
    # Salida
    print(numeros_invertidos)