
billetes_monedas=0
cantidad=0
desglosar_cantidad=0
cantidad_cop=0

cantidad_cop = int(input("Ingrese la cantidad entera de COP: "))

desglose = desglosar_cantidad

print("Desglose de la cantidad:")
for valor, cantidad in desglose.items():
        if cantidad > 0:
            print(f"{cantidad} x {valor} COP")


for valor in sorted(billetes_monedas, reverse=True):
        if cantidad >= valor:
            billetes_monedas[valor] = cantidad // valor
            cantidad %= valor

