""" Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Escribir un algoritmo que determine la hora de llegada a la ciudad B. """

HH= int(input("HH: "))
MM= int(input("MM: "))
SS= int(input("SS: "))

T= int(input("Segundos de viaje: "))

segSalida= HH*3600+MM*60+SS
tiempoViaje= T+segSalida

HH= tiempoViaje/3600
MM= (tiempoViaje%3600)/60
SS= ((tiempoViaje%3600)%60)/60

print("Llegará a las %d:%d:%d"%(HH,MM,SS))