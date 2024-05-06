""" Escribe un programa que pida un número
entero entre uno y doce e imprima el número de días que tiene el mes correspondiente. """

num= float(input("Numero de mes: "))

if num==2:
    dias= 28
elif num==1 or num==3 or num==5 or num==7 or num==8 or num==10 or num==12:
    dias=31
else:
    dias=30

print(dias,"días")