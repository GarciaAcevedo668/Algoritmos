
#def calcular_nuevo_sueldo(sueldo,aumento1,aumento2,nuevo_sueldo):
    
sueldo = 0
aumento_uno = 0
aumento_dos = 0
nuevo_sueldo_uno=0
nuevo_sueldo_dos=0
sueldo=float(input("Registre el sueldo del trabajador :" ))

if sueldo < 900000:
   aumento_uno=float(sueldo * 0.15)
   nuevo_sueldo_uno = sueldo + aumento_uno

else: 
     #sueldo < 900000
 aumento_dos= float(sueldo * 0.12)
 nuevo_sueldo_dos = sueldo + aumento_dos



print("El sueldo del trabajador es :", sueldo )    
print("El aumento de sueldo al 15% es ", aumento_uno )
print("El sueldo total al 15% es ", nuevo_sueldo_uno )

print("El aumento de sueldo al 12% es ", aumento_dos )
print("El sueldo total al 12% es ", nuevo_sueldo_dos )
