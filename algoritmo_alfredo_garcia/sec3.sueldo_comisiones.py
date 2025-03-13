#3.	Un vendedor recibe un sueldo base, más un 10% extra por comisiones de sus ventas.
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas
# que realizó en el mes y el total que recibirá tomando en cuenta su sueldo base y sus comisiones.


sueldo = 0
ventas = 0
comision = 0

sueldo = int(input("Por favor ingrese el sueldo del trabajador "))

ventas1 = int(input("Por favor ingrese el valor de las ventas1 "))
ventas2 = int(input("Por favor ingrese el valor de las ventas2 "))
ventas3 = int(input("Por favor ingrese el valor de las ventas3 "))

ventas=ventas1+ventas2+ventas3

comisiones=(ventas*0.1)


Total_sueldo = (sueldo + ventas + comisiones)

print(("El total de sueldos mas comisiones es ", Total_sueldo))

