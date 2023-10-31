# Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
# usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
# asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
# asignaturas que el usuario tiene que repetir.

def obtener_notas(asignaturas):
    notas = []
    for asignatura in asignaturas:
        nota_valida = False
        while not nota_valida:
            nota_input = input(f"Ingrese la nota de {asignatura}: ")
            if nota_input.replace(".", "", 1).isdigit():
                nota = float(nota_input)
                if 0 <= nota <= 10:
                    notas.append(nota)
                    nota_valida = True
                else:
                    print("Error: La nota debe estar entre 0 y 10.")
            else:
                print("Error: Por favor, ingrese un número válido para la nota.")
                return []
    return notas

def asignaturas_repetir(asignaturas, notas):
    asignaturas_repetir = []
    for i in range(len(asignaturas)):
        nota_str = str(notas[i])
        if nota_str.replace(".", "", 1).isdigit():
            nota_float = float(nota_str)
            if 0 <= nota_float < 5.0:
                asignaturas_repetir.append(asignaturas[i])
    return asignaturas_repetir

if __name__ == "__main__":
    # Entrada
    asignaturas = input("Ingrese las asignaturas del curso separadas por comas: ").split(',')
    # Proceso
    notas = obtener_notas(asignaturas)
    asignaturas_repetir = asignaturas_repetir(asignaturas, notas)
    # Salida
    print("Asignaturas que debe repetir:")
    for asignatura in asignaturas_repetir:
        print(asignatura)