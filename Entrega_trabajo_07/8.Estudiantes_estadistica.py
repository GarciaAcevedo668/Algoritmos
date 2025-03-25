
#9 estudiantes
cantidad=int(input("Ingrse la cantidad de usuarios a registrar"))
#puntaje=float(input("Ingrse el puntaje del alumno a registrar "))
lista_cantidad=[]
lista_nombre=[]
lista_puntaje=[]
for i in range(cantidad):
    nombre=input("Ingrese el nombre del alumno ")
    #cantidad=float(input("Ingrese el puntaje del alumno "))
    puntaje=float(input("Ingrese el puntaje del alumno "))
    lista_cantidad.append(cantidad)
    lista_nombre.append(nombre)
    lista_puntaje.append(puntaje)
    
    print("el puntaje mas alto es ",max(lista_cantidad))
    #print("el puntaje mas alto es ", lista_nombre.index{0})
    
    print("la lista de nombres es: ", lista_nombre+ lista_puntaje)
    print("la lista de puntaje es:", lista_puntaje)
