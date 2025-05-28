"""
Pedro está organizando un evento en su Universidad. El evento será en el mes de abril, comenzando y terminando en dicho mes.
El problema es: Pedro quiere calcular la duración del evento en segundos, sabiendo obviamente el comienzo y el final del mismo.
Sabes que el evento puede durar de unos pocos segundos a algunos días, así que debes ayudar a Pedro
a calcular el tiempo total correspondiente a la duración del evento.

Entrada
La primera línea de la entrada contiene información sobre el día de inicio del evento en el formato "Dia xx". La siguiente línea contiene la hora de inicio del evento
en el formato presentado en la entrada de muestra. Luego, 2 líneas de entrada con el mismo formato, correspondientes al final del evento.

Salida
Su programa debe imprimir la siguiente salida, una información por línea, considerando que si cualquier información 
es nula por ejemplo, el número 0 debe imprimirse en lugar de W, X, Y o Z:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que el evento del caso de prueba tiene duración mínima de un minuto.

Ejemplo de entrada	
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

Ejemplo de salida
3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)


"""

"""
"""
#****************************************************************************
from datetime import datetime, time

#Entrada de la fecha incial o mas antigua
formato_fecha_hora_inicial = "%d/%m/%Y %H:%M:%S"
fecha_inicial_ingresada_str = input(f"Introduce la fecha y hora inicial por favor (ej. {datetime.now().strftime(formato_fecha_hora_inicial)}): ")
fecha_inicial_dt = datetime.strptime(fecha_inicial_ingresada_str, formato_fecha_hora_inicial)


print(fecha_inicial_dt.strftime("%d/%m/%Y %H:%M:%S"))



#Entrada de la fecha final o mas reciente 
formato_fecha_hora_final = "%d/%m/%Y %H:%M:%S"
fecha_final_ingresada_str = input(f"Introduce la fecha y hora final por favor (ej. {datetime.now().strftime(formato_fecha_hora_final)}): ")
fecha_final_dt = datetime.strptime(fecha_final_ingresada_str, formato_fecha_hora_final)
print(fecha_final_dt.strftime("%d/%m/%Y %H:%M:%S"))

if fecha_final_dt < fecha_inicial_dt:
    print("\n  ¡ADVERTENCIA! La fecha final es anterior a la fecha inicial.")
    print("  El cálculo del tiempo transcurrido no procederá. Por favor, reinicia el programa con fechas válidas.")
    # Si la fecha final es menor, el programa TERMINA aquí.
    exit() # Detiene la ejecución del script

# --- 5. Realizar la resta de fechas (solo si la fecha final es >= a la inicial) ---
diferencia = fecha_final_dt - fecha_inicial_dt
#realizar la resta de fechas 
diferencia = fecha_final_dt - fecha_inicial_dt
dias_transcurridos = diferencia.days
segundos_resto_del_dia = diferencia.seconds

horas_transcurridas = segundos_resto_del_dia // 3600    # 3600 segundos en una hora
minutos_transcurridos = (segundos_resto_del_dia % 3600) // 60 # Resto de segundos (no horas), dividido por 60
segundos_transcurridos = segundos_resto_del_dia % 60    # Resto de segundos (no horas ni minutos)

print(f"  Fecha y Hora Inicial: {fecha_inicial_dt.strftime(formato_fecha_hora_inicial)}")
print(f"  Fecha y Hora Final  : {fecha_final_dt.strftime(formato_fecha_hora_final)}")

# Una validación para el orden de las fechas

if fecha_final_dt < fecha_inicial_dt:
    print("\n  ¡Advertencia! La fecha final es anterior a la fecha inicial. Los resultados serán negativos o cero.")

print(f"  Días: {dias_transcurridos}")
print(f"  Horas: {horas_transcurridas}")
print(f"  Minutos: {minutos_transcurridos}")
print(f"  Segundos: {segundos_transcurridos}")

#dias transcurridos
#print(f"  Días: {dias_transcurridos}")









"""""
print("\n--- RESUMEN DE FECHAS SELECCIONADAS ---")
print(f"  Fecha y Hora Inicial: {fecha_inicial_dt.strftime(formato_fecha_hora_inicial)}")
print(f"  Fecha y Hora Final  : {fecha_final_dt.strftime(formato_fecha_hora_final)}")
"""""






# 3. Intentas convertir la cadena ingresada por el usuario



