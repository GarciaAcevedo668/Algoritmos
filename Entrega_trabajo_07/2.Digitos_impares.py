#2.Imprimir todos los enteros positivos impares menores que 100, omitiendo los divisibles por 7

for n in range(1,100):
    if n%7 != 0 and n % 2 != 0:
     print(n) 
