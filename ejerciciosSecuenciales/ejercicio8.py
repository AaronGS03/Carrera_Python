""" Un vendedor recibe un sueldo base mas un 10% extra por comisión
de sus ventas, el vendedor desea saber cuanto dinero obtendrá por 
concepto de comisiones por las tres ventas que realiza en el mes y 
el total que recibirá en el mes
tomando en cuenta su sueldo base y comisiones. """

venta= float(input("Sueldo: "))
comision= venta*0.10

dineroTotal= (venta+comision)*3
dineroComisiones= dineroTotal-(venta*3)

print("Ganará",dineroTotal,"€ en total,",dineroComisiones,"en comisiones")