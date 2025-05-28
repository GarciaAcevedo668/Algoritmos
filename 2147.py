 #Define el tiempo que toma escribir un solo carácter (en segundos)

TIEMPO_POR_CARACTER = 0.01

# Lee la cantidad de casos de prueba


# Lee la cantidad de casos de prueba
try:
    C = int(input())
except ValueError:
    print("Entrada inválida para la cantidad de casos de prueba. Por favor, introduce un número entero.")
    exit() # Termina el programa si la entrada inicial no es válida

# Procesa cada caso de prueba
for _ in range(C):
    # Lee la palabra
    palabra = input()

    # Calcula el tiempo empleado
    # La longitud de la palabra es len(palabra)
    # Tiempo = número de caracteres * tiempo por carácter
    tiempo_empleado = len(palabra) * TIEMPO_POR_CARACTER

    # Imprime el tiempo empleado
    # Usamos .2f para formatear el número a dos decimales, lo cual es común
    # en problemas de programación competitiva para la salida de tiempos.
    print(f"{tiempo_empleado:.2f}")