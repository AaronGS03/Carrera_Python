""" Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los 
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si sólo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno. """

A= float(input("A: "))
B= float(input("B: "))
C= float(input("C: "))

if A**2==(B**2+C**2):
    print("Rectángulo")
elif (A==B and A!=C) or (A==C and A!=C):
    print("Isósceles")
elif A==B==C:
    print("Equilatero")
else: 
    print("Escaleno")