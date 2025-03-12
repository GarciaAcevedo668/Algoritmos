#7.	Dada una cantidad en metros, se requiere que la convierta a pies y pulgadas,
# considerando lo siguiente: 1 metro = 39.27 pulgadas; 1 pie = 12 pulgadas.

metros=0
pulgadas=0
pies=0

metros = 39.27*int(input("Por favor ingrese total de metros a convertir "))

pulgadas=metros/39.2701
pies=pulgadas/12



#print("el total de pulgadas para", metros, " es ", pulgadas )
print("el total de pulgadas para en pies es ", pies )


