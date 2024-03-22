""" Programa que lea una cadena por teclado y compruebe si es una letra mayúscula. """

cha= input("letra: ")

if cha.isupper():
    print(cha,"es mayúscula")
else:
    print(cha,"es minúscula")