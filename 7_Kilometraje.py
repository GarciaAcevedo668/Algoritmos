#Variables 
distancia_km=int(input("Por Favor registre los kilometros rrecorridos "))
                 

if distancia_km <= 300:
        costo = 50000
elif distancia_km > 300 and distancia_km < 1000:        
    #elif 300 > distancia_km < 1000:
        costo_base = 70000
        costo_km_adicional = 30000 * (distancia_km - 300)
        costo = costo_base + costo_km_adicional
else:
        costo_base = 150000
        costo_km_adicional = 9000 * (distancia_km - 1000)
        costo = costo_base + costo_km_adicional
        
print("Para menos de 300 el pago es :", costo)