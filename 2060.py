def desafio_de_bino():
    """
    Lee una lista de números y cuenta cuántos son múltiplos de 2, 3, 4 y 5.
    Imprime los conteos en el formato especificado.
    """
    N = int(input())  # Lee la cantidad de números en la lista

    # Lee la línea completa de números y los convierte a enteros
    numeros_str = input().split()
    lista_numeros = [int(num) for num in numeros_str]

    # Inicializa contadores para cada múltiplo
    multiplos_de_2 = 0
    multiplos_de_3 = 0
    multiplos_de_4 = 0
    multiplos_de_5 = 0

    # Itera sobre cada número en la lista
    for numero in lista_numeros:
        # Verifica si es múltiplo de 2
        if numero % 2 == 0:
            multiplos_de_2 += 1
        
        # Verifica si es múltiplo de 3
        if numero % 3 == 0:
            multiplos_de_3 += 1
            
        # Verifica si es múltiplo de 4
        if numero % 4 == 0:
            multiplos_de_4 += 1
            
        # Verifica si es múltiplo de 5
        if numero % 5 == 0:
            multiplos_de_5 += 1

    # Imprime los resultados en el formato requerido
    print(f"{multiplos_de_2} Multiplo(s) de 2")
    print(f"{multiplos_de_3} Multiplo(s) de 3")
    print(f"{multiplos_de_4} Multiplo(s) de 4")
    print(f"{multiplos_de_5} Multiplo(s) de 5")
desafio_de_bino()  # Llama a la función para ejecutar el desaf