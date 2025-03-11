

compras=int(input("Favor registre el valor de la compras total :" ))

if compras > 5000000 :
    
    contado = compras*55/100
    pres_banco = compras*30/100
    pres_fabricante = compras-contado-pres_banco
    
    print("Valor pago de contado ", contado)
    print("Valor del prestamo al banco ", pres_banco)
    print("Valor del prestamo al fabricante ", pres_fabricante)
    
elif compras<5000000 :  
    contado = compras*0.70
    pres_fabricante = compras*0.30
    
    
    print("Valor pago de contado ", contado)
    print("Valor del prestamo al fabricante ", pres_fabricante)
    
    