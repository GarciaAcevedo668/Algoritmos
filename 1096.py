def imprimir_secuencia_especifica():
    """
    Imprime la secuencia I=X J=Y siguiendo el patrón especificado:
    I de 1 a 9 (saltando de 2 en 2), y para cada I, J de 7 a 5 (decrementando de 1 en 1).
    """
    # Bucle exterior para la variable I
    # range(1, 10, 2) significa: empieza en 1, termina antes de 10, salta de 2 en 2.
    # Esto generará: 1, 3, 5, 7, 9
for i in range(1, 10, 2):
        # Bucle interior para la variable J
        # range(7, 4, -1) significa: empieza en 7, termina antes de 4, decrementa de 1 en 1.
        # Esto generará: 7, 6, 5
    for j in range(7, 4, -1):
     
        print(f"I={i} J={j}")

# Llama a la función para ejecutar el programa
#if __name__ == "__main__":
#    imprimir_secuencia_especifica()