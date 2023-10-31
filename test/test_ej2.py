
from src.Ejercicio_2 import generar_mensajes_asignaturas, mostrar_asignaturas

def test_generar_mensajes_asignaturas():
    assert generar_mensajes_asignaturas(["Mates", "Ingles"]) == "Yo estudio Mates\nYo estudio Ingles"
    assert generar_mensajes_asignaturas([""]) == "Yo estudio "