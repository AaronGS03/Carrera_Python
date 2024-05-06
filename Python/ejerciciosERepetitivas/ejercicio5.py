""" Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio. """

num= input("Caracter?(0:Salir): ")

while not num.isspace():
    if num.lower()==("a" or "e" or "i" or "o" or "u"):
        print("VOCAL")
    else:
        print("NO VOCAL")
    num= input("Letra?(Espacio:Salir): ")

        