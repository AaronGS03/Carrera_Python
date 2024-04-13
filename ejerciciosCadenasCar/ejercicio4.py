""" Suponiendo que hemos introducido una cadena por 
teclado que representa una frase (palabras separadas por espacios),
 realiza un programa que cuente cuantas palabras tiene. """

string=input("Cad:")

cant= len(string.strip().split(" "))

print(cant,"palabras")