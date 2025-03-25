saldo=1000
 
print("\t.:MENU:.")                    
print("\t1. Depositar dinero.")
print("\t2. Retirar dinero.")
print("\t3. Consultar saldo.")
print("\t4. Salir.")
opcion = int(input("Digite una opcion de menu : "))

print()

if opcion == 1:
    consignacion = float(input("Cuanto Dinero desea depositar: "))
    saldo += consignacion
    print("Su saldo actual es: ", saldo)
elif opcion == 2:
    retiro = float(input("Digite la cantidad de dinero a retirar: "))
    if retiro > saldo:
        print("No tiene esa cantidad de dinero ")
        saldo -= retiro
        print("Su saldo actual es: ", saldo)
elif opcion == 3:
    print("Su saldo actual es: ", saldo)
elif opcion == 4:
    print("Gracias por utilizar nuestros servicios.")
else:
    print("Opcion invalida, por favor digite una opcion valida.")
    