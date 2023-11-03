# Escribir un programa que pregunte por una muestra de números, 
# separados por comas, los guarde en una lista y muestre por 
# pantalla su media y desviación típica.

def es_numero_valido(numero):
    if not numero:
        return False
    if numero.count('.') > 1 or numero.count(',') > 1:
        return False
    numero = numero.replace(',', '.')
    if numero.replace('.', '').isdigit() or (numero[0] == '-' and numero[1:].replace('.', '').isdigit()):
        return True
    return False

def es_muestra_valida(muestra):
    numeros = muestra.replace(',', '.').split('.')
    for numero in numeros:
        if not es_numero_valido(numero) or float(numero) < 0:
            return False
    return True

def calcular_media(numeros):
    suma = sum(numeros)
    media = suma / len(numeros)
    return media

def calcular_desviacion_tipica(numeros, media):
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    desviacion_tipica = (suma_cuadrados / len(numeros)) ** 0.5
    return desviacion_tipica

if __name__ == "__main__":
    # Entrada
    muestra_numeros = input("Ingrese una muestra de números separados por comas o puntos: ")
    # Procesamiento
    while not es_muestra_valida(muestra_numeros):
        muestra_numeros = input("Error: Por favor, ingrese solo números positivos separados por comas o puntos: ")
    lista_numeros = [float(numero) for numero in muestra_numeros.replace(',', '.').split('.')]
    media = calcular_media(lista_numeros)
    desviacion_tipica = calcular_desviacion_tipica(lista_numeros, media)
    # Salida
    print(f"Media: {round(media, 2)}")
    print(f"Desviación Típica: {round(desviacion_tipica, 2)}")