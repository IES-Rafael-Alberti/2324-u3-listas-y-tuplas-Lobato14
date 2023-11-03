from src.Ejercicio_13 import es_numero_valido, es_muestra_valida, calcular_media, calcular_desviacion_tipica

def test_es_numero_valido():
    assert es_numero_valido("123")
    assert es_numero_valido("-123")
    assert es_numero_valido("12.34")
    assert es_numero_valido("-12.34")
    assert not es_numero_valido("12..34")
    assert not es_numero_valido("-12..34")
    assert not es_numero_valido("abc")
    assert not es_numero_valido("12a")
    assert not es_numero_valido("-12a")

def test_es_muestra_valida():
    assert es_muestra_valida("1.2.3.4.5")
    assert not es_muestra_valida("1,,3,4,5")
    assert not es_muestra_valida("1.2..3.4.5")
    assert not es_muestra_valida("abc")
    assert not es_muestra_valida("1,a,3,4,5")

def test_calcular_media():
    assert calcular_media([1, 2, 3, 4, 5]) == 3.0
    assert calcular_media([-1, 0, 1, 2, 3]) == 1.0
    assert calcular_media([2, 4, 6, 8, 10]) == 6.0

def test_calcular_desviacion_tipica():
    assert calcular_desviacion_tipica([1, 2, 3, 4, 5], 3.0) == 1.4142135623730951
    assert calcular_desviacion_tipica([-1, 0, 1, 2, 3], 1.0) == 1.4142135623730951
    assert calcular_desviacion_tipica([2, 4, 6, 8, 10], 6.0) == 2.8284271247461903