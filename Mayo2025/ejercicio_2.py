#Ejercicio 2
#Recorre un diccionario y crea una lista solo con los valores que contiene, sin añadir valores
#duplicados.
"""""

valores={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}

lista=[]

numeros_unicos = set(valores)

for i in numeros_unicos:
     lista.append(i)   

print(numeros_unicos)

#• Resultado: [3, 8, 12, 5, 7]
"""""

valores={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}

valores_unicos = set()
for valor in valores.values():
    valores_unicos.add(valor)

lista_sin_duplicados = list(valores_unicos)

print(lista_sin_duplicados)