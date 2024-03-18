#Pide la edad y diga si es mayor de edad.
edad= int(input("Edad: "))
if edad>=18:
    print("Mayor de edad")

#Con comas, se añaden solos los espacios
print("Tu edad es",edad,"años")

#También se puede hacer con concatenación, pero hay que convertir
#a string y no pone espacios
print("Tu edad es"+str(edad)+"años")