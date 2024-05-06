""" Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás. """

string= input("Cad: ")
if string==string[::-1]:
    print("Palindromo")
else:
    print("No palíndromo")