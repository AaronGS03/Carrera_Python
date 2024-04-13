""" Pide una cadena y un carácter por teclado (valida que sea un carácter)
 y muestra cuantas veces aparece el carácter en la cadena """


string=input("Cad:")
error=True
while error:
    car=input("Caracter:")
    if len(car)==1:
        error=False
    else:
        print("solo un caracter")
print("Ese caracter aparece:",string.count(car),"veces")
