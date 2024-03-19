""" Realiza un programa que reciba una cantidad de 
minutos y muestre por pantalla a cuantas horas y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos. """

min= float(input("min: "))

h= int(min/60)
m= min%60

print(min,"minutos son",h,"horas y",m,"min")