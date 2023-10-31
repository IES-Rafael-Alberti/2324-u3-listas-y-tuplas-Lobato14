from src.Ejercicio_8 import es_palindromo

def test_es_palindromo():
    # Caso de prueba con palabra palíndroma
    palabra_palindroma = "reconocer"
    resultado = es_palindromo(palabra_palindroma)
    assert resultado == True
    
    # Caso de prueba con palabra no palíndroma
    palabra_no_palindroma = "python"
    resultado = es_palindromo(palabra_no_palindroma)
    assert resultado == False

    # Caso de prueba con palabra con espacios
    palabra_con_espacios = "anita lava la tina"
    resultado = es_palindromo(palabra_con_espacios)
    assert resultado == True

    # Caso de prueba con palabra con números
    palabra_con_numeros = "12321"
    resultado = es_palindromo(palabra_con_numeros)
    assert resultado == True

    # Caso de prueba con palabra vacía
    palabra_vacia = ""
    resultado = es_palindromo(palabra_vacia)
    assert resultado == True

    # Caso de prueba con palabra de un solo carácter
    palabra_un_caracter = "a"
    resultado = es_palindromo(palabra_un_caracter)
    assert resultado == True

    # Caso de prueba con palabra no palíndroma
    palabra_no_palindroma = "hola"
    resultado = es_palindromo(palabra_no_palindroma)
    assert resultado == False