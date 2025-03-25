#8.consumo licor

consumidores=input("Consume licor ")
if consumidores == "S":
    licor_preferido=int(input("Licor preferido (1-Aguardiente,2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro)"))
    edad=int(input("Edad "))
    sexo=input("Sexo ")
    if sexo == "Mujer" and edad < 18:
        print("Mujer menor de edad")
    elif sexo == "Hombre" and licor_preferido != 1 and 20:
        print("Hombre que no consume aguardiente y tiene entre 20 y 25 años")
    elif licor_preferido == 3:
        print("Promedio de edad de quienes consumen cerveza")
    elif licor_preferido == 5:
        print("Porcentaje de personas que consumen whisky respecto al total encuestado")
    else:
        print("No cumple con ninguno de los criterios")
else:
    print("No consume licor")
    print("Total de personas encuestadas que consumen licor")
    print("Total de mujeres menores de edad")
    print("Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años")
    print("Promedio de edad de quienes consumen cerveza")
    print("Porcentaje de personas que consumen whisky respecto al total encuestado")
    print("¿Desea continuar con la encuesta?")  # Pregu