def calcular_intereses_reinversion(capital_inicial, tasa_interes_anual, anos):
    """
    Calcula los intereses generados y el capital final con reinversión si los intereses exceden $100.000 COP.

    Args:
        capital_inicial (float): El capital inicial invertido.
        tasa_interes_anual (float): La tasa de interés anual (en decimal, por ejemplo, 0.05 para 5%).
        anos (int): El número de años de la inversión.

    Returns:
        tuple: Una tupla con los intereses totales generados y el capital final.
    """

    capital_actual = capital_inicial
    intereses_totales = 0

    for _ in range(anos):
        intereses_anuales = capital_actual * tasa_interes_anual
        intereses_totales += intereses_anuales

        if intereses_anuales > 100000:
            capital_actual += intereses_anuales  # Reinversión

    return intereses_totales, capital_actual

# Ejemplo de uso
capital_inicial = 1000000  # 1 millón de COP
tasa_interes_anual = 0.10  # 10% anual
anos = 5

intereses_totales, capital_final = calcular_intereses_reinversion(capital_inicial, tasa_interes_anual, anos)

print(f"Intereses totales generados: ${intereses_totales:,.2f} COP")
print(f"Capital final: ${capital_final:,.2f} COP")