def redondear_a_centena(a, b, c, d):
   
 n = a * 1000 + b * 100 + c * 10 + d

  #decenas_unidades=0
  #n_redondeado=0 
  
 decenas_unidades = c * 10 + d
 
 if decenas_unidades >= 50:
  n_redondeado = (n // 100 + 1) * 100
 else:
  n_redondeado = (n // 100) * 100
   
 return n_redondeado

# Ejemplos de uso

#int(input("Introduzca el numero a1 " ))   #, b1, c1, d1 = 2, 3, 6, 2
#int(input("Introduzca el numero b1 " ))
#int(input("Introduzca el numero c1 " ))
#int(input("Introduzca el numero d1 " ))

a1, b1, c1, d1 = 2, 3, 6, 2  
resultado = redondear_a_centena(a1, b1, c1, d1)

print(f"El número {a1}{b1}{c1}{d1} redondeado es: {resultado}")  # Salida: 2400

a2, b2, c2, d2 = 2, 3, 4, 2
resultado = redondear_a_centena(a2, b2, c2, d2)
print(f"El número {a2}{b2}{c2}{d2} redondeado es: {resultado}")  # Salida: 2300

a3, b3, c3, d3 = 2, 9, 6, 2
resultado = redondear_a_centena(a3, b3, c3, d3)
print(f"El número {a3}{b3}{c3}{d3} redondeado es: {resultado}")  # Salida: 3000






