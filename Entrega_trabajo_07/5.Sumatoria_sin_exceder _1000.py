#5.El programa calcula el número de términos necesarios para que la siguiente sumatoria se aproxime a 1000 sin excederlo:
SUMA=0
K=1
while SUMA<1000:
    SUMA+=K
    K+=1
    print("La suma de los números enteros positivos es:", SUMA-1)
    print("El número de términos necesarios es:", K-1)
    
print()