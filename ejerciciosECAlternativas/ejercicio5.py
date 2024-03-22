""" Escribe un programa que pida un nombre de usuario y una contraseña y 
si se ha introducido “pepe” y “asdasd” 
se indica “Has entrado al sistema”, sino se da un error. """

nombre = input("Nombre?: ")
cont = input("Contraseña?: ")

if nombre=="pepe" and cont=="asdasd":
    print("Has entrado al sistema")
else:
    print("Error")