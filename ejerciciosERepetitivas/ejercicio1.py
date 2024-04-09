""" Crea una aplicación que pida un número y calcule su factorial
(El factorial de un número es el producto de todos los enteros
entre 1 y el propio número y se representa por el número 
seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120), """

num= int(input("Num?: "))
acum=1

if(num==0):
    print("0! = 1")
else:
    for var in range(1,num+1,+1):
        acum= var*acum
    print(num,"! =",acum)