""" Algoritmo que pida tres números y los muestre ordenados (de mayor a menor); """

n1= float(input("Numero 1: "))
n2= float(input("Numero 2: "))
n3= float(input("Numero 3: "))

if n1>n2 and n1>n3:
        if n2>n3:
            print(n1,n2,n3)
        else:
            print(n1,n3,n2)
elif n2>n3 and n2>n1:
        if n1>n3:
            print(n2,n1,n3)
        else:
            print(n2,n3,n1)
else:
    if n2>n1:
        print(n3,n2,n1)
    else:
        print(n3,n1,n2)