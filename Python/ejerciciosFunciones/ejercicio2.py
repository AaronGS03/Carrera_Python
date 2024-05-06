"""Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo. """

def EsMultiplo(num1,num2):
    if num1%num2==0:
        return True
    else: 
        return False

num1= int(input("Num1: "))
num2= int(input("Num2: "))

print("Es multiplo?:",EsMultiplo(num1,num2))