
from src.Ejercicio_2 import generar_mensajes_asignaturas

def test_generar_mensajes_asignaturas():
    assert generar_mensajes_asignaturas([""]) == "Error: Ingresa un nombre válido para la asignatura."
    assert generar_mensajes_asignaturas(["123"]) == "Error: Ingresa un nombre válido para la asignatura."
    assert generar_mensajes_asignaturas(["Mates", ""]) == "Error: Ingresa un nombre válido para la asignatura."

def test_generar_mensajes_asignaturas():
    assert generar_mensajes_asignaturas(["Mates", "Ingles"]) == "Yo estudio Mates\nYo estudio Ingles"
    try:
        generar_mensajes_asignaturas([""])
    except ValueError as e:
        assert str(e) == "Error: Ingresa un nombre válido para la asignatura."
    else:
        assert False, "Se esperaba una excepción ValueError pero no se lanzó."