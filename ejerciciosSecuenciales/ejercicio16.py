""" Dos vehículos viajan a diferentes velocidades (v1 y v2) 
y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor.
Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km)y sus respectivas velocidades (km/h) 
y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro. """

v1= float(input("V1(km/h): "))
v2= float(input("V2(km/h): "))
dist= float(input("Dist (km): "))

tiempo= dist*60/(v1-v2)

print("Tarda %.2f minutos"%tiempo)