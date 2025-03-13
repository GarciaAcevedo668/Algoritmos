#9.Calcular el salario neto de un trabajador en función del número de horas trabajadas, el precio de la hora
# y considerando un descuento fijo al sueldo base por concepto de impuestos del 20%.

salario = 0
horas_trabajadas = 0
valor_hora = 0
impuestos=0


horas_trabajadas = int(input("Por favor ingrese el numero de horas trabajadas "))
valor_hora = int(input("Por favor ingrese el valor de la hora "))

salario = horas_trabajadas*valor_hora
impuestos= salario*0.2
salario_neto=salario-impuestos

print(("El total del salario del trabajador ", salario))
print(("El total del impuesto del trabajador ", impuestos))
print(("Valor neto recibido por e trabajador ", salario_neto ))

