# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las 
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def multiplosAbecedario(abecedario):
    abecedario_filtrado = [abecedario[letra] 
                           for letra in range(len(abecedario)) 
                                if (letra + 1) % 3 != 0]
    return abecedario_filtrado

if __name__ == "__main__":
    # Entrada
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    # Proceso
    abecedario_filtrado = multiplosAbecedario(abecedario)
    # Salida
    print(abecedario_filtrado)