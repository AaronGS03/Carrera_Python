""" Escribir un programa que convierta un valor dado
en grados Fahrenheit a grados Celsius. 
Recordar que la fórmula para la conversión es: C = (F-32)*5/9"""

F= float(input("Grados Fº: "))

C= (F-32)*5/9

print(F,"grados Farenheit son %.2f grados centígrados"%(C))