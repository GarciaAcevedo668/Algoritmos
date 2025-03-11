#def calcular_resultado(A, B, C, D):
    

#"""
#    Calcula el resultado basado en la condición dada para D.

#    Args:
#        A: Primer número.
#        B: Segundo número.
#        C: Tercer número.
#        D: Cuarto número (condición).

#    Returns:
#        El resultado del cálculo o un mensaje de error.
#    """

A=int(input("Registre el numero A deseado :" ))
B=int(input("Registre el numero B deseado :" ))
C=int(input("Registre el numero C deseado :" ))
D=int(input("Registre el numero D deseado :" ))



if D == 0:
      E=(A - C) ** 2
      print("el valor resultado de la ecuacion es :", E)

elif D>0:
     F=(A - B) ** 3 / D
     print("el valor resultado de la ecuacion es :", F)


