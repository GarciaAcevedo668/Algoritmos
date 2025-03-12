#10.El cambio de divisas en la bolsa de Madrid el 25/08/1987 fue el siguiente 100
# chelines austríacos	=	956.871 pesetas
#1 dólar EEUU	=	122.499 pesetas
#100 dracmas griegos =	88.607 pesetas
#100 francos belgas	=	323.728 pesetas
#1 franco francés	=	20.110 pesetas
#1 libra esterlina	=	178.938 pesetas
#100 liras italianas	=	9.289 pesetas
#Lea una cantidad en chelines austriacos e imprima
# el equivalente en pesetas. Lea una cantidad en dracmas griegos e imprima su equivalente en francos franceses.
# Finalmente, lea una cantidad en pesetas e imprima su equivalente en dólares y liras italianas.

chelines_austriacos=956.871/100
dolar=122.499 #0.0135
dracma_griego=88.607/100   #0.01925
francos_belgas=323.728/100
franco_frances=20.110  #51.94646
libra_esterlina=178.938
liras_italianas=9.289/100

# 1. Lea una cantidad en chelines austriacos e imprima

#pesetas_chelines=float(input("Escriba la cantidada de Chelines austriacos "))
#valor = pesetas_chelines/chelines_austriacos

#print("El valor de",pesetas_chelines, "chelines australianos es de ", valor)

#2. convertir dracmas_griegos a francos_franceses

#dracma_griegos=float(input("Escriba la cantidad de dracmas griegos "))
#valor_francos = dracma_griegos/franco_frances
#print("El valor de",dracma_griegos, "chelines australianos es de ", valor_francos)

#3. convertir pesetas a dolares

pesetas=float(input("Escriba la cantidada de pesetas a convertir "))

valor_pesetas = pesetas*dolar
valor_pesetas2 = pesetas*liras_italianas

print("El valor de",pesetas, "el valor de las pesetas en dolares es ", valor_pesetas)
print("El valor de",pesetas, "el valor de las pesetas en dolares es ", valor_pesetas2)

