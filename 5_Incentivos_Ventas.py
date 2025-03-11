

def calcular_salarios(ventas_departamento1, ventas_departamento2, ventas_departamento3, salario_base, numero_vendedores):
    """
    Calcula el salario total de los vendedores en cada departamento.

    Args:
        ventas_departamento1: Ventas del departamento 1.
        ventas_departamento2: Ventas del departamento 2.
        ventas_departamento3: Ventas del departamento 3.
        salario_base: Salario base de cada vendedor.
        numero_vendedores: Numero de vendedores por departamento.

    Returns:
        Un diccionario con el salario total para cada departamento.
    """

    ventas_totales = ventas_departamento1 + ventas_departamento2 + ventas_departamento3
    porcentaje_incentivo = 0.33
    porcentaje_extra = 0.20

    salarios = {}

    # Departamento 1
    salario_departamento1 = salario_base * numero_vendedores
    if ventas_departamento1 > ventas_totales * porcentaje_incentivo:
        salario_departamento1 *= 1 + porcentaje_extra
    salarios["Departamento 1"] = salario_departamento1

    # Departamento 2
    salario_departamento2 = salario_base * numero_vendedores
    if ventas_departamento2 > ventas_totales * porcentaje_incentivo:
        salario_departamento2 *= 1 + porcentaje_extra
    salarios["Departamento 2"] = salario_departamento2

    # Departamento 3
    salario_departamento3 = salario_base * numero_vendedores
    if ventas_departamento3 > ventas_totales * porcentaje_incentivo:
        salario_departamento3 *= 1 + porcentaje_extra
    salarios["Departamento 3"] = salario_departamento3

    return salarios

# Ejemplo de uso:
ventas_dpto1 = 10000
ventas_dpto2 = 12000
ventas_dpto3 = 8000
salario_vendedor = 2000
numero_vendedores = 10

resultados = calcular_salarios(ventas_dpto1, ventas_dpto2, ventas_dpto3, salario_vendedor, numero_vendedores)

for departamento, salario in resultados.items():
    print(f"{departamento}: ${salario:.2f}")