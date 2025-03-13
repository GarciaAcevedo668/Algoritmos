#12.	Calcule y muestre, a un alumno, cuál será su promedio general en las tres materias;
# más difíciles que cursa y cuál será el promedio que obtendrá en cada una de ellas.
# Estas materias se evalúan como se muestra a continuación:

#Matemática		Examen 90% y	10% del promedio de tres tareas.
#Física		Examen 80% y	20% del promedio de dos tareas.
#Química		Examen 85% y	15% del promedio de tres tareas.

matematicas1= float(input("Regsitre la nota 1 de matematicas "))
matematicas2= float(input("Regsitre la nota 2 de matematicas "))
matematicas3= float(input("Regsitre la nota 3 de matematicas "))
examenmatematicas= float(input("Regsitre la nota examen de matematicas "))

promedio_matematicas=((matematicas1+matematicas2+matematicas3)/3)*0.1+examenmatematicas*0.9

print("la nota pomedio de matematicas queda en ", promedio_matematicas)

fisica1= float(input("Regsitre la nota 1 de fisica1 "))
fisica2= float(input("Regsitre la nota 2 de fisica2 "))
fisica3= float(input("Regsitre la nota 3 de fisica3 "))
examenfisica= float(input("Regsitre la nota examen de fisica "))

promedio_fisica=((fisica1+fisica2+fisica3)/3)*0.2+examenfisica*0.8+examenfisica*0.8

print("la nota pomedio de fisica queda en ", promedio_fisica )
                  
quimica1= float(input("Regsitre la nota 1 de quimica1 "))
quimica2= float(input("Regsitre la nota 2 de quimica2 "))
quimica3= float(input("Regsitre la nota 3 de quimica3 "))
examenquimica= float(input("Regsitre la nota examen de quimica "))

promedio_quimica=((quimica1+quimica2+quimica3)/3)*0.15+examenquimica*0.85

print("la nota pomedio de fisica queda en ", promedio_quimica )



