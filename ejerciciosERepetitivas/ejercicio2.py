""" Crea una aplicación que permita adivinar un número.
La aplicación genera un número aleatorio del 1 al 100. 
A continuación va pidiendo números y va respondiendo si el
número a adivinar es mayor o menor que el introducido,a demás 
de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número 
(además te dice en cuantos intentos lo has acertado), si se llega al
limite de intentos te muestra el número que había generado. """

import random

intentos=10
num= random.randint(1,100)
win= False
while win==False:
    intentos-=1
    guess= int(input("Numero?: "))
    if guess==num:
        win=True
        print("Acertaste en",10-intentos,"intentos!")
    elif guess>num:
        print("Es menor. Te quedan",intentos,"intentos")
    elif guess<num:
        print("Es mayor. Te quedan",intentos,"intentos")
    if intentos==0:
        print("El numero era:",num)
        intentos=10
        num=random.randint(1,100)