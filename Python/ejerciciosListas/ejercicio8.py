""" Queremos guardar los nombres y la edades de los alumnos de un curso.
Realiza un programa que introduzca el nombre y la edad de cada alumno.
El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*)
Al finalizar se mostrará los siguientes datos:

Todos lo alumnos mayores de edad.
Los alumnos mayores (los que tienen más edad) """

nom= input("Nombre: ")
lista=[]
while nom != "*":
    edad= int(input("edad: "))
    lista.append([nom,edad])
    nom= input("Nombre: ")
for alumno in lista:
    if alumno[1]>=18:
        print(alumno[0],alumno[1])
    