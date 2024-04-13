""" Realizar un programa que compruebe si una cadena contiene una subcadena. 
Las dos cadenas se introducen por teclado. """

string= input("Cad:")
sub= input("Sub:")

if sub in string:
    print("Contiene la sub")
else:
    print("No contiene la sub")