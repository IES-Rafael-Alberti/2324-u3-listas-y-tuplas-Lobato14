# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
# Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la 
# lista.

def generar_mensajes_asignaturas(asignaturas):
    mensajes = []
    for asignatura in asignaturas:
        mensajes.append("Yo estudio " + asignatura)
    return "\n".join(mensajes)

def mostrar_asignaturas(asignaturas):
    return generar_mensajes_asignaturas(asignaturas)

if __name__ == "__main__":
    asignaturas = []
    introducir_asig = "si"
    while introducir_asig.lower() == "si":
        asignatura = input("Escribe una asignatura: ")
        if asignatura.isalpha() and asignatura != "":
            asignaturas.append(asignatura)
            introducir_asig = input("¿Deseas introducir otra asignatura a la lista? (si/no): ")
            while introducir_asig.lower() not in ["si", "no"]:
                print("Error: Por favor, ingresa 'si' o 'no'.")
                introducir_asig = input("¿Deseas introducir otra asignatura a la lista? (si/no): ")
        else:
            print("Error: Ingresa un nombre válido para la asignatura.")
            introducir_asig = "si"
    mensajes_asignaturas = mostrar_asignaturas(asignaturas)
    print(mensajes_asignaturas)