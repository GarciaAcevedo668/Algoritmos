#6.	Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay
#en un grupo de estudiantes.


mujeres = int(input("Por favor ingrese total mujeres estudiantes "))
hombres = int(input("Por favor ingrese total hombres estubidantes "))


total_alumnos=mujeres+hombres
 
porcentaje_hombres = float(hombres/total_alumnos*100)

porcentaje_mujeres = float(mujeres/total_alumnos*100)

print(("el porcentaje de hombres estudiantes es ", porcentaje_hombres))
print(("el porcentaje de hombres estudiantes es ", porcentaje_mujeres))
