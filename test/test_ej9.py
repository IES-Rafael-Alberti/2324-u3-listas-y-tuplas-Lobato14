from src.Ejercicio_9 import contar_vocales

def test_contar_vocales():
    # Caso de prueba con una palabra sin vocales
    resultado = contar_vocales("hola")
    assert resultado == {'a': 1, 'e': 0, 'i': 0, 'o': 1, 'u': 0}

    # Caso de prueba con una palabra que contiene todas las vocales
    resultado = contar_vocales("murcielago")
    assert resultado == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

    # Caso de prueba con una palabra que contiene solo una vocal
    resultado = contar_vocales("casa")
    assert resultado == {'a': 2, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Caso de prueba con una palabra que contiene todas las vocales repetidas
    resultado = contar_vocales("murcielago aeiou")
    assert resultado == {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}

    # Caso de prueba con una palabra que contiene números y caracteres especiales
    resultado = contar_vocales("murcielago123!@#$")
    assert resultado == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}