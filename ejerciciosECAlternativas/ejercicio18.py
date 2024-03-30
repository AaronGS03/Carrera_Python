""" Realiza un programa que pida el día de la semana (del 1 al 7) y 
escriba el día correspondiente. Si introducimos otro número nos da un error. """

resultado= int(input("Resultado: "))

err= False

if resultado==1:
    opuesto="Lunes"
elif resultado==2:
    opuesto="Martes"
elif resultado==3:
    opuesto="Miércoles"
elif resultado==4:
    opuesto="Jueves"
elif resultado==5:
    opuesto="Viernes"
elif resultado==6:
    opuesto="Sábado"
elif resultado==7:
    opuesto="Domingo"
else:
    err=True

if err:
    print("Error: Numero incorrecto")
else:
    print("Hoy es:",opuesto)