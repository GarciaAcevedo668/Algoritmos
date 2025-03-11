

lectura_actual=0
lectura_anterior=0
monto_aseo=0
monto_total=0
calcular_monto_luz=0
calcular_monto_aseo=0


lectura_anterior = int(input("Ingrese la lectura anterior en Kwh: "))
lectura_actual = int(input("Ingrese la lectura actual en Kwh: "))
calcular_monto_luz=lectura_anterior-lectura_actual
calcular_monto_aseo= calcular_monto_luz

#monto_luz = calcular_monto_luz(lectura_anterior, lectura_actual)
#monto_aseo = calcular_monto_aseo(monto_luz)
monto_total = calcular_monto_luz + calcular_monto_aseo

consumo = lectura_actual - lectura_anterior
if consumo <= 100:
        costo_kwh = 4600
elif consumo <= 300:
        costo_kwh = 80000
elif consumo <= 500:
        costo_kwh = 100000
else:
        costo_kwh = 120000

monto_luz = consumo * costo_kwh

print(f"Monto a pagar por consumo de luz eléctrica: {monto_luz:,.2f} COP")
print(f"Monto a pagar por servicio de aseo urbano: {monto_aseo:,.2f} COP")
print(f"Monto total a pagar: {monto_total:,.2f} COP")

    