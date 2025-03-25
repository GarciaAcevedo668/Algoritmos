#6.Division-metodo resta
contador=0
Dividendo=int(input("Ingrese Dividendo "))
Divisor=int(input("Ingrese Divisor "))

while Dividendo>Divisor:
    Dividendo=Dividendo - Divisor
    contador=contador+1
            
print("El valor restante o residuo es: ", Dividendo)
print("El el valor cuociente es: ", contador)
