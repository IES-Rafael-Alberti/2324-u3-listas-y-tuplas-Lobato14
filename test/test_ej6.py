from src.Ejercicio_6 import asignaturasRepetidas

def test_asignaturas_repetidas():
    # Caso de prueba con notas válidas
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = ["4.5", "6.0", "3.8"]
    asignaturas_repetir = asignaturasRepetidas(asignaturas, notas_input)
    assert asignaturas_repetir == ["Matemáticas", "Química"]

    # Caso de prueba con notas inválidas
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = ["abc", "6.0", "3.8"]
    asignaturas_repetir = asignaturasRepetidas(asignaturas, notas_input)
    assert asignaturas_repetir == []

    # Caso de prueba con notas fuera de rango
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = ["11.0", "6.0", "-3.8"]
    asignaturas_repetir = asignaturasRepetidas(asignaturas, notas_input)
    assert asignaturas_repetir == []

    # Caso de prueba con notas válidas pero sin asignaturas
    asignaturas = []
    notas_input = []
    asignaturas_repetir = asignaturasRepetidas(asignaturas, notas_input)
    assert asignaturas_repetir == []

    # Caso de prueba con notas válidas y asignaturas pero sin asignaturas a repetir
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = ["8.5", "9.0", "7.8"]
    asignaturas_repetir = asignaturasRepetidas(asignaturas, notas_input)
    assert asignaturas_repetir == []

    # Caso de prueba con notas válidas y asignaturas aprobadas
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = ["8.5", "4.5", "3.8"]
    asignaturas_repetir = asignaturasRepetidas(asignaturas, notas_input)
    assert asignaturas_repetir == ["Física", "Química"]

    # Caso de prueba con notas válidas, asignaturas aprobadas y asignaturas vacías
    asignaturas = []
    notas_input = []
    asignaturas_repetir = asignaturasRepetidas(asignaturas, notas_input)
    assert asignaturas_repetir == []