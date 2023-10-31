# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha 
# sacado en cada asignatura, y después las muestre por pantalla con el mensaje En 
# <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la 
# lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

def ingresar_notas(asignaturas, notas_input):
    notas = []
    for i in range(len(asignaturas)):
        nota_valida = False
        while not nota_valida:
            nota_input = notas_input[i].replace(",", ".", 1)  # Reemplaza ',' por '.' si es un número decimal
            if nota_input.replace(".", "", 1).isdigit():
                nota = float(nota_input)
                if 0 <= nota <= 10:
                    notas.append(nota)
                    nota_valida = True
                else:
                    return "Error: La nota debe estar entre 0 y 10."
            else:
                return "Error: Por favor, ingresa un número válido."
    return notas

def solicitar_notas_asignaturas(asignaturas):
    notas_input = []
    for asignatura in asignaturas:
        nota = input(f"Ingresa la nota de {asignatura}: ")
        notas_input.append(nota)
    return notas_input

if __name__ == "__main__":
    # Entrada
    asignaturas = ["Matemáticas", "Física", "Química"]
    notas_input = solicitar_notas_asignaturas(asignaturas)
    # Proceso
    notas = ingresar_notas(asignaturas, notas_input)
    for i in range(len(asignaturas)):
        # Salida
        print(f"En {asignaturas[i]} has sacado {notas[i]}")