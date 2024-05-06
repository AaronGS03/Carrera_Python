""" Realiza un programa que pida por teclado el resultado (dato entero)
obtenido al lanzar un dado de seis caras y muestre por pantalla el número en 
letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje:
“ERROR: número incorrecto.”.
Ejemplo:

Introduzca número del dado: 5
En la cara opuesta está el "dos". """

resultado= int(input("Resultado: "))

error=False

if resultado==1:
    opuesto="seis"
elif resultado==2:
    opuesto="cinco"
elif resultado==3:
    opuesto="cuatro"
elif resultado==4:
    opuesto="tres"
elif resultado==5:
    opuesto="dos"
elif resultado==6:
    opuesto="uno"
else:
    error=True

if error:
    print("Error: Numero incorrecto")
else:
    print("En la cara opuesta está el:",opuesto)