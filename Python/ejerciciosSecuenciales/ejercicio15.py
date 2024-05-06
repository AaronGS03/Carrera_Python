""" Dadas dos variables numéricas A y B, que el usuario debe teclear,
se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre
cuanto valen al final las dos variables. """

A= float(input("A: "))
B= float(input("B: "))

print("Valores pre-cambio A:",A,"B:",B)

C=A
A=B
B=C

print("Valores cambiados A:",A,"B:",B)