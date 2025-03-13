#8.	Calcule el área de un triángulo en función de las longitudes de sus lados, utilizan la fórmula:	 
import math

a=0
b=0
c=0
s=0

a=float(input(" Registre por favor el lado a del triangulo :" ))
b=float(input(" Registre por favor el lado b del triangulo :" ))
c=float(input(" Registre por favor el lado c del triangulo :" ))

s=float(a+b+c)/2

Area = math.sqrt(s*((s-a)*(s-b)*(s-c)))

print("El semiperimetro es : ", s)

print("El area del triangulo es : ", Area )


