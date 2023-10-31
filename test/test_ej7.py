from src.Ejercicio_7 import multiplosAbecedario

def test_multiplosAbecedario():
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    resultado = multiplosAbecedario(abecedario)
    assert resultado == ['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'v', 'w', 'y', 'z']