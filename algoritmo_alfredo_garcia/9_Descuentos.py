monto_compra=int(input("digite el valor de la compra: "))
if monto_compra < 50000:
        descuento = 0
elif 50000 <= monto_compra <= 100000:
        descuento = 0.05
elif 100000 < monto_compra <= 700000:
        descuento = 0.11
elif 700000 < monto_compra <= 1500000:
        descuento = 0.18
else:
        descuento = 0.25

print("El valor del descuentos por compras menores a  50.000 es :", descuento*0)
print("El valor del descuentos por compras entre 50.000 y 100.000 es :", descuento*0.05)

