from src.Ejercicio_10 import sacarNumMenor, sacarNumMayor

def test_sacarNumMenor():
    assert sacarNumMenor([50, 75, 46, 22, 80, 65, 8]) == 8

def test_sacarNumeroMayor():    
    assert sacarNumMayor([50, 75, 46, 22, 80, 65, 8]) == 80