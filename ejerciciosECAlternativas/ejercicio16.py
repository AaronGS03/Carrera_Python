""" La política de cobro de una compañía telefónica es: cuando se
realiza una llamada, el cobro es por el tiempo que ésta dura,
de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes
tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en
turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada. """

tiempo=int(input("Tiempo: "))
domingo= bool(input("Domingo? "))
turnoM= bool(input("Turno de mañana? "))

if tiempo<=5:
    precio=1
elif tiempo>5 and tiempo<=8:
    precio=1.80
elif tiempo>8 and tiempo<=10:
    precio= 2.50
elif tiempo>10:
    precio=3

if domingo:
    precio+=precio*0.3
else:
    if turnoM:
        precio+=precio*0.15
    else:
        precio+=precio*0.10

print("Precio llamada:",precio)