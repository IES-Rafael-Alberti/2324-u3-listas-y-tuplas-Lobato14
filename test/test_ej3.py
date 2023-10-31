from src.Ejercicio_3 import solicitar_notas_asignaturas

def test_solicitar_notas_asignaturas(mocker):
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = ["8", "9.5", "7.2"]

    mocker.patch("builtins.input", side_effect=notas_input)

    notas_obtenidas = solicitar_notas_asignaturas(asignaturas)
    assert notas_obtenidas == notas_input