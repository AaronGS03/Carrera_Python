""" Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. 
Pueden ocurrir tres cosas:

El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo. """

n1= float(input("Base: "))
n2= float(input("Exponente: "))

if n1>0:
    print(pow(n1,n2))
elif n2==0:
    print(1)
elif n2<0:
    print(pow(n1,1/n2))