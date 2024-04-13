""" Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado. """

num= float(input("Num:"))

for var in range(0, 11):
    print(var,"*",num,"=",var*num)