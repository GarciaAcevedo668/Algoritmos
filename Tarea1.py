#def calcular_intereses_reinversion(capital_inicial, tasa_interes_anual, anos):



capital_inicial=0
intereses_totales=0   
años=0
capital_actual=capital_inicial
tiempo=años
tasa_interes_año_uno=0
intereses_año_uno=0
intereses_acumulados=0
liquidacion_intereses=0


capital_actual= float(input("Ingrese el capital incial : "))
tasa_interes_anual=float(input("Ingrese la tasa de interes anual "))
liquidacion_intereses= capital_actual * tasa_interes_anual*tiempo

if liquidacion_intereses > 100000:
            capital_actual += liquidacion_intereses  # Reinversión

else:
   
  intereses_acumulados += liquidacion_intereses
  
#tiempo=int(input("Ingrese los años trascurridos del Ahorro "))
#intereses_año_uno = capital_actual * tasa_interes_anual*tiempo
#intereses_totales += intereses_anuales

print("Capital Inicial {:.2f}".format(capital_actual))
print("Tasa de interes anual ", tasa_interes_anual)
print("Tiempo transcurrido ", tiempo)
print("Liquidacion intereses {:.2f}".format(liquidacion_intereses))
#print("Intereses Acumulados {:.2f}".format(intereses_acumulados))
