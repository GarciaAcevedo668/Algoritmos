#Ejercicio 1
#Crea un programa que recorra una lista y cree un diccionario que contenga el número de veces que
#aparece cada número en la lista.

lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
diccionario_conteo = {}

for numero in lista:
    if numero in diccionario_conteo:
        diccionario_conteo[numero] += 1
    else:
        diccionario_conteo[numero] = 1

print(diccionario_conteo)