""" Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es 
bisiesto si es un número divisible por 4,
pero no si es divisible por 100, excepto que también sea divisible por 400. """

año = int(input("Año: "))

if año%4==0 and (año%100!=0 or año%400==0):
    print("bisiesto")
else:
    print("no bisiesto")