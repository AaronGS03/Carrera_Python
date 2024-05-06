""" Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
 Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior. """

def calcularMaxMin(lista):
    return [max(lista),min(lista)]

lista=[]
while len(lista)<10:
    num= int(input("NUm: "))
    lista.append(num)

print(calcularMaxMin(lista))