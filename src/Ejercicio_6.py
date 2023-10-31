# Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
# usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
# asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
# asignaturas que el usuario tiene que repetir.

def asignaturasRepetidas(asignaturas, notas_input):
    asignaturas_repetir = []
    indice = 0
    while indice < len(asignaturas):
        asignatura = asignaturas[indice]
        try:
            nota = float(notas_input[indice])
            if 0 <= nota <= 10:
                if nota < 5.0:
                    asignaturas_repetir.append(asignatura)
            else:
                print(f"Error: La nota de {asignatura} debe estar entre 0 y 10.")
        except ValueError:
            print(f"Error: Por favor, ingresa un número válido para la nota de {asignatura}.")
        indice += 1
    return asignaturas_repetir

if __name__ == "__main__":
    # Entrada
    asignaturas_input = input("Ingresa las asignaturas del curso separadas por comas: ").split(',')
    notas_input = input("Ingresa las notas correspondientes separadas por comas: ").split(',')
    # Proceso
    asignaturas_repetir = asignaturasRepetidas(asignaturas_input, notas_input)
    # Salida
    print("Asignaturas que debes repetir:")
    for asignatura in asignaturas_repetir:
        print(asignatura)