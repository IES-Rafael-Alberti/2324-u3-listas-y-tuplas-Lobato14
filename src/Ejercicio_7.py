# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las 
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def multiplosAbecedario(abecedario):
    del abecedario[::3]
    return abecedario

if __name__ == "__main__":
    # Entrada
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    # Proceso
    abecedario_filtrado = multiplosAbecedario(abecedario)
    # Salida
    print(abecedario_filtrado)