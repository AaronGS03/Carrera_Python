

peso= float(input("Kiloramos: "))

if peso>5:
    print("Rechazo de la entrega")
else:
    print("1.- América del Norte")
    print("2.- América Central")
    print("3.- América del Sur")
    print("4.- Europa")
    print("5.- Asia")
    zona = int(input("A que zona se reparte (1-5):"))
    if zona == 1:
        print("Coste:",peso*24, "euros.")
    elif zona == 2:
        print("Coste:",peso*20, "euros.")
    elif zona == 3:
        print("Coste:",peso*21, "euros.")
    elif zona == 4:
        print("Coste:",peso*10, "euros.")
    elif zona == 5:
        print("Coste:",peso*18, "euros.")
    else:
        print("Zona incorrecta.")