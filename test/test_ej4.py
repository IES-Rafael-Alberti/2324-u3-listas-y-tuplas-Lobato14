from src.Ejercicio_4 import ordenar_numeros

def test_ordenar_numeros():
    assert ordenar_numeros("Hola") == "Error: Por favor, ingresa solo números separados por espacios."
    assert ordenar_numeros("-4 -4 +4") == "Error: Por favor, ingresa solo números separados por espacios."
    assert ordenar_numeros("4 2 0 21") == [0, 2, 4, 21]