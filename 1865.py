# 1. Leer la cantidad de casos de prueba
try:
    C = int(input())
except ValueError:
    print("Entrada inválida. Por favor, introduce un número entero para la cantidad de casos de prueba.")
    exit()

# 2. Iterar por cada caso de prueba
for _ in range(C):
    # 3. Leer el nombre y la fuerza
    linea = input().split() # Lee la línea completa (nombre y fuerza)
    nombre = linea[0]       # El nombre es la primera palabra
    # fuerza = int(linea[1]) # La fuerza es el segundo valor, pero no la usaremos por la lógica de Mjolnir

    # 4. Determinar si la persona es digna e imprimir 'Y' o 'N'
    if nombre == "Thor": # Asumimos que solo Thor es digno de levantar Mjolnir
        print("Y")
    else:
        print("N")

