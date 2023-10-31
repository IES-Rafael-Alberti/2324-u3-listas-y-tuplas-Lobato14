
from src.Ejercicio_2 import mostrar_asignaturas

def test_mostrar_asignaturas(mocker, capsys):
    input_values = ["Matemáticas", "Física", "no"]
    mocker.patch("builtins.input", side_effect=input_values)
    
    mensajes_asignaturas = mostrar_asignaturas([])
    
    captured = capsys.readouterr()
    assert "Yo estudio Matemáticas\nYo estudio Física" in captured.out
    assert mensajes_asignaturas == "Yo estudio Matemáticas\nYo estudio Física"

def test_entrada_invalida_letras(mocker, capsys):
    input_values = ["", " ", "123", "Matemáticas", "Física", "no"]
    mocker.patch("builtins.input", side_effect=input_values)
    
    mensajes_asignaturas = mostrar_asignaturas([])
    
    captured = capsys.readouterr()
    assert "Error: Ingresa un nombre válido para la asignatura." in captured.out
    assert mensajes_asignaturas == "Error: Ingresa un nombre válido para la asignatura."

def test_entrada_invalida_vacia(mocker, capsys):
    input_values = ["", " ", "no"]
    mocker.patch("builtins.input", side_effect=input_values)
    
    mensajes_asignaturas = mostrar_asignaturas([])
    
    captured = capsys.readouterr()
    assert "Error: Por favor, ingresa 'si' o 'no'." in captured.out
    assert mensajes_asignaturas == "Error: Por favor, ingresa 'si' o 'no'."