from src.Ejercicio_5 import anadirListaNum

def test_anadirListaNum():
    lista = []
    anadirListaNum(lista)
    assert lista == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_numeros_invertidos():
    lista = []
    anadirListaNum(lista)
    numeros_invertidos = ", ".join(str(num) for num in lista)
    assert numeros_invertidos == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1"