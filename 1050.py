#Lea un número entero que corresponda al número de código de área para marcación telefónica.
# A continuación, imprima el destino de acuerdo con la siguiente tabla:


Telefonos={"61":"Brasilia","71":"Salvador","11":"Sao Paulo","21":"Rio de Janeiro","32":"Juz de Fora","19":"Campinas","27":"Victoria","31":"Belo Horizonte",}

while True:
    
    clave=input("Por favor digite el numero de DDD ")
    if clave in Telefonos:
        valor = Telefonos[clave]
        print(f"{clave}  {valor}")
        break
    else:
        print("DDD")
