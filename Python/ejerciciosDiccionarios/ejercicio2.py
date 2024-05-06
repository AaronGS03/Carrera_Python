""" Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena. """

cadena= input("String: ")

dicc= {}
cont=0

while cont < len(cadena):
    if cadena[cont] in dicc:
        dicc[cadena[cont]]+=1
    else:
        dicc[cadena[cont]]=1
    cont+=1

print(dicc)