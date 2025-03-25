#Numero perfecto

n=int(input("Ingrese un numero " ))
i=2
suma=0
while i <= n:
    if n % i == 0:
        suma += n//i
    i += 1
    
if suma == n:
    print(n,"es un numero perfecto ")
else:
    print(n,"no es un numero perfecto ")
