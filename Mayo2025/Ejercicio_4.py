def gestionar_notas():
    estudiantes = {}
    num_estudiantes = 0
    max_estudiantes = 5

    print("Programa para introducir notas de estudiantes (máximo 10).")

    while num_estudiantes < max_estudiantes:
        num_estudiantes += 1
        id_estudiante = str(num_estudiantes)  # Usamos el número como ID
        nombre = input(f"Introduce el nombre del estudiante {id_estudiante}: ")
        while True:
            #try:
                nota_str = input(f"Introduce la nota de {nombre}: ")
                nota = float(nota_str.replace(',', '.'))  # Permite coma o punto como separador decimal
                if 0 <= nota <= 10:
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
           # except ValueError:
           #     print("Por favor, introduce un número válido para la nota.")

        estudiantes[id_estudiante] = {
            "nombre": nombre,
            "nota": nota
        }

        if num_estudiantes < max_estudiantes:
            continuar = input("¿Desea introducir otro estudiante? (s/n): ").lower()
            if continuar != 's':
                break

    # Procesar los datos
    suspendidos = []
    aprobados = []
    suma_notas = 0

    for id_estudiante, datos in estudiantes.items():
        nombre = datos["nombre"]
        nota = datos["nota"]
        suma_notas += nota
        if nota < 5:
            suspendidos.append(nombre)
        else:
            aprobados.append(nombre)

    # Mostrar resultados
    print("\n--- Resultados ---")
    if suspendidos:
        print("Estudiantes suspendidos:", ", ".join(suspendidos))
    else:
        print("No hay estudiantes suspendidos.")

    if aprobados:
        print("Estudiantes aprobados:", ", ".join(aprobados))
    else:
        print("No hay estudiantes aprobados.")

    if estudiantes:
        media = suma_notas / len(estudiantes)
        print(f"Nota media de la clase: {media:.2f}")
    else:
        print("No se introdujeron notas.")

# Ejecutar el programa
gestionar_notas()