#7.Altura de ESTUDIANTES


max_altura=0
lista_altura=[]
cantidad=int(input("Ingrse la cantidad de usuarios a registrar"))
for l in range(0,cantidad):
    altura=float(input("Ingrese la altura del usuario "))
    lista_altura.append(altura)

for i in range(len(lista_altura)):
    if max_altura<lista_altura[i]:
       max_altura=lista_altura[i]
    else:   
       max_altura=max_altura
print("La altura mas alta es ",max_altura )   
    