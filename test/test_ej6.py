from src.Ejercicio_6 import asignaturas_repetir

def test_asignaturas_repetir():
    # Caso de prueba con notas válidas y asignaturas a repetir
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = [4.5, 6.0, 3.8]
    asignaturas_repetidas_resultado = asignaturas_repetir(asignaturas, notas_input)
    assert asignaturas_repetidas_resultado == ["Matemáticas", "Química"]

    # Caso de prueba con notas válidas y sin asignaturas a repetir
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = [8.5, 9.0, 7.8]
    asignaturas_repetidas_resultado = asignaturas_repetir(asignaturas, notas_input)
    assert asignaturas_repetidas_resultado == []

    # Caso de prueba con notas válidas, asignaturas aprobadas y asignaturas vacías
    asignaturas = []
    notas_input = []
    asignaturas_repetidas_resultado = asignaturas_repetir(asignaturas, notas_input)
    assert asignaturas_repetidas_resultado == []

    # Caso de prueba con notas válidas y asignaturas aprobadas
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = [8.5, 4.5, 3.8]
    asignaturas_repetidas_resultado = asignaturas_repetir(asignaturas, notas_input)
    assert asignaturas_repetidas_resultado == ["Física", "Química"]

    # Caso de prueba con notas inválidas
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = ["abc", 6.0, -3.8]
    asignaturas_repetidas_resultado = asignaturas_repetir(asignaturas, notas_input)
    assert asignaturas_repetidas_resultado == []

    # Caso de prueba con notas fuera de rango
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = [11.0, 6.0, -3.8]
    asignaturas_repetidas_resultado = asignaturas_repetir(asignaturas, notas_input)
    assert asignaturas_repetidas_resultado == []

    # Caso de prueba con notas válidas pero sin asignaturas
    asignaturas = []
    notas_input = []
    asignaturas_repetidas_resultado = asignaturas_repetir(asignaturas, notas_input)
    assert asignaturas_repetidas_resultado == []

    # Caso de prueba con notas inválidas y asignaturas
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = ["abc", "def", "ghi"]
    asignaturas_repetidas_resultado = asignaturas_repetir(asignaturas, notas_input)
    assert asignaturas_repetidas_resultado == []