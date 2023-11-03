# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha 
# sacado en cada asignatura, y después las muestre por pantalla con el mensaje En 
# <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la 
# lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


def anadirAsignatura(asignaturas, notas):
    asignaturas_repetir = []
    for indice in range(len(asignaturas)):
        if notas[indice] < 5:
            asignaturas_repetir.append(asignaturas[indice])
    return asignaturas_repetir

if __name__ == "__main__":
    # Entrada
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas = []
    asignaturas_repetir = []
    # Proceso
    for asignatura in asignaturas:
        nota_valida = False
        while not nota_valida:
            nota_input = input(f"Ingresa la nota de {asignatura}: ").replace(",", ".", 1)
            if nota_input.replace(".", "", 1).isdigit():
                nota = float(nota_input)
                if 0 <= nota <= 10:
                    notas.append(nota)
                    nota_valida = True
                else:
                    print("Error: La nota debe estar entre 0 y 10.")
            else:
                print("Error: Por favor, ingresa un número válido.")

    resultado = anadirAsignatura(asignaturas)

    # Salida
    for indice in range(len(asignaturas)):
        print(f"En {asignaturas[indice]} has sacado {notas[indice]}")

    if asignaturas_repetir:
        print("Debes repetir las siguientes asignaturas:")
        for asignatura in asignaturas_repetir:
            print(asignatura)
    else:
        print("¡Felicidades! Has aprobado todas las asignaturas.")