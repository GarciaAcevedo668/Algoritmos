#3. El programa calcula la suma de todos los números pares en el rango de 97 a 1003.
suma_pares = 0
for n in range(97,1003):
    if n % 2 == 0:
        suma_pares += n
print("La suma de los números pares es:", suma_pares)
