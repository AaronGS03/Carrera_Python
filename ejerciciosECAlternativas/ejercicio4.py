""" Crea un programa que pida al usuario dos números
y muestre su división si el segundo no es cero,
o un mensaje de aviso en caso contrario. """

n1= float(input("Numero 1: "))
n2= float(input("Numero 2: "))

if n2!=0:
    print(n1/n2)
else:
    print("Num 2 no puede ser 0")
    