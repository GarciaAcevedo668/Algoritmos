Algoritmo ejercicio_6
	Escribir "Ingrese el año respectivo"
	Leer año
	
	Si ((año mod 4=0) y (año mod 100 <> 0)) O año mod 4 = 0   Entonces
		
		Escribir "El año es bisiesto "
	SiNo
			Escribir "El año no es bisiesto "
	
Fin Si
	
FinAlgoritmo
