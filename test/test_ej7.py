from src.Ejercicio_7 import multiplosAbecedario

def test_multiplosAbecedario():
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    resultado = multiplosAbecedario(abecedario)
    assert resultado == ['b', 'c', 'e', 'f', 'h', 'i', 'k', 'l', 'n', 'o', 'q', 'r', 't', 'u', 'w', 'x', 'z']