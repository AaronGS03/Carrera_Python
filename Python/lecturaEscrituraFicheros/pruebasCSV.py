import csv
fichero=open("lecturaEscrituraFicheros/ejemplo2.csv","r")

#Para evitar conflicto con las comillas de los datos
contenido=csv.reader(fichero,quotechar='"')

for row in contenido:
    print(row)

#Devuelve:
""" 
['A??o', 'Marca', 'Modelo', 'Descripci??n', 'Precio']
['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00']
['1999', 'Chevy', 'Venture "Extended Edition"', '', '4900.00']
['1999', 'Chevy', 'Venture "Extended Edition, Very Large"', '', '5000.00']
['1996', 'Jeep', 'Grand Cherokee', 'MUST SELL!]
[air, moon roof, loaded', '4799.00'] """