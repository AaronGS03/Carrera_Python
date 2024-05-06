""" Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos). """

m2e= int(input("Cantidad de monedas de 2€: "))
m1e= int(input("Cantidad de monedas de 1€: "))
m50c= int(input("Cantidad de monedas de 50c: "))
m20c= int(input("Cantidad de monedas de 20c: "))
m10c= int(input("Cantidad de monedas de 10c: "))

print("Tienes: %.2f€"%(m2e*2+m1e*1+m50c*0.5+m20c*0.20+m10c*0.10))