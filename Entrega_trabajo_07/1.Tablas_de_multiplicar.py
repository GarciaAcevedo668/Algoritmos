#1.El programa solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.
factor=0   

t=int(input("Por favor digite un numero entero "))
factor=int(input("Favor digitar el numero de la tabla a multiplicar "))

for t in range(1,11):
    #multiplicacion=7*t #hecemos la multiplicacion
    print(f'{factor} x {t} = {factor*t}') #mostramos el resultado