""" Realizar un programa que comprueba si una cadena leída por teclado 
comienza por una subcadena introducida por teclado. """

string= input("Cad:")
sub= input("Sub:")

if string.startswith(sub):
    print("Comienza por la sub")
else:
    print("No comienza por la sub")