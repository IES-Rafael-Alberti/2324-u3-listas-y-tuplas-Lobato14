
from src.Ejercicio_3 import anadirAsignatura

def test_anadirAsignatura():
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas = [4, 6, 3]
    assert anadirAsignatura(asignaturas, notas) == ["Matemáticas", "Química"]

    asignaturas = ["Matemáticas", "Física", "Química"]
    notas = [7, 8, 9]
    assert anadirAsignatura(asignaturas, notas) == []

    asignaturas = ["Matemáticas", "Física", "Química"]
    notas = [5, 3, 5]
    assert anadirAsignatura(asignaturas, notas) == ["Física"]