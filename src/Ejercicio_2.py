# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
# Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la 
# lista.

def generar_mensajes_asignaturas(asignaturas):
    mensajes = []
    for asignatura in asignaturas:
        if asignatura.isalpha() and asignatura != "":
            mensajes.append("Yo estudio " + asignatura)
        else:
            raise ValueError("Error: Ingresa un nombre válido para la asignatura.")
    return "\n".join(mensajes)

def mostrar_asignaturas(asignaturas):
    try:
        mensajes = generar_mensajes_asignaturas(asignaturas)
        return mensajes
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    # Entrada
    asignaturas = []
    introducir_asig = "si"
    # Procesamiento
    while introducir_asig.lower() == "si":
        asignatura = input("Escribe una asignatura: ")
        try:
            if asignatura.isalpha() and asignatura != "":
                asignaturas.append(asignatura)
                introducir_asig = input("¿Deseas introducir otra asignatura a la lista? (si/no): ")
                while introducir_asig.lower() not in ["si", "no"]:
                    print("Error: Por favor, ingresa 'si' o 'no'.")
                    introducir_asig = input("¿Deseas introducir otra asignatura a la lista? (si/no): ")
            else:
                raise ValueError("Ingresa un nombre válido para la asignatura.")
        except ValueError as ve:
            print("Error:", ve)
            introducir_asig = "si"

    mensajes_asignaturas = mostrar_asignaturas(asignaturas)
    # Salida
    print(mensajes_asignaturas)