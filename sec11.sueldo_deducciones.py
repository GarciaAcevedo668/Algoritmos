#11.Se conoce de un trabajador su nombre, el número de horas normales trabajadas,
# el pago de una hora normal y el número de horas extras trabajadas.
# Además, que, cada hora extra se paga 25% más del valor de una hora normal. 
# Si se deducen al trabajador sobre el sueldo base 5% del pago forzoso, 
# 2% de política habitacional y 7% para caja de ahorro.
# Si se le asignan 250.000 COP por actualización académica, 173.000 COP
# por cada hijo y una prima por hogar de 180000 COP. 
# Calcule y muestre las asignaciones, las deducciones
# y el sueldo neto del trabajador para el mes de diciembre.

horas_normales=0
valor_hora_normal=0
horas_extras=0

horas_normales=float(input("regristre las horas normales "))
valor_hora_normal=float(input("registre el valor de la hora normal "))
liquidacion_normales=horas_normales*valor_hora_normal

horas_extras=float(input("regristre las horas extras "))
valor_hora_extra=valor_hora_normal*1.25

liquidacion_total=liquidacion_normales+valor_hora_extra                     


dedu_pago_forzoso=liquidacion_total*0.05
dedu_politica_habitacional=liquidacion_total*0.02
dedu_ahorro=liquidacion_total*0.07
actualizacion_academica=250000
hijo=173000
prima_hogar=180000

sueldo_neto=(liquidacion_total+actualizacion_academica+hijo+prima_hogar-dedu_pago_forzoso-dedu_politica_habitacional-dedu_politica_habitacional)

print("Asignacion de actualizacion academica ",actualizacion_academica)
print("Asignacion por hijo ", hijo)
print("Asignacion por prima de hogar ", prima_hogar)
print("deduciones por pago forsozo ", dedu_pago_forzoso)
print("deduciones por politica habitacional ", dedu_politica_habitacional)
print("deduciones para ahorro ", dedu_ahorro)
print("valor del sueldo neto ", sueldo_neto)

