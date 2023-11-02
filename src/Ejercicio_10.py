# Escribir un programa que almacene en una lista los siguientes precios: 
# 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de 
# los precios.

def sacarNumMenor(listaPrecios):
    return min(listaPrecios)

def sacarNumMayor(listaPrecios):
    return max(listaPrecios)

if __name__ == "__main__":
    # Entrada
    listaPrecios = [50, 75, 46, 22, 80, 65, 8]
    # Proceso
    numMenor = sacarNumMenor(listaPrecios)
    numMayor = sacarNumMayor(listaPrecios)
    # Salida
    print("El número minimo de la lista es ", numMenor)
    print("El número mayor de la lista es ", numMayor)