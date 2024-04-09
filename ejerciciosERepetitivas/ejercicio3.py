""" Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos. """


num= float(input("Num?(0:Salir): "))
ac=0
cont=0

while num!=0:
    ac=ac+num
    cont+=1
    num= float(input("Num?(0:Salir): "))
if ac!=0:
    media= ac/cont
    print(ac, media)
else:
    print(0, 0)