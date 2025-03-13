discriminante=0

a = float(input("Ingrese el coeficiente A: "))
b = float(input("Ingrese el coeficiente B: "))
c = float(input("Ingrese el coeficiente C: "))

x1=0
x2=0

if discriminante == 0:
        x1 = x2 = -b / (2*a)
#return x1, x2
elif discriminante > 0:
     #-b=0
 x1 = (-b + math.sqrt(discriminante)) / (2*a)
 x2 = (-b - math.sqrt(discriminante)) / (2*a)
#        return x1, x2
    

soluciones = resolver_ecuacion_cuadratica(a, b, c)

if isinstance(soluciones, tuple):
        print(f"X1 = {soluciones[0]:.2f}")
        print(f"X2 = {soluciones[1]:.2f}")
else:
        print(soluciones)   