""" Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final. """

import math
mediaParciales= (float(input("Nota 1er parcial: "))+float(input("Nota 2o parcial: "))+float(input("Nota 3er parcial: ")))*0.55/3
notaEFinal= float(input("Nota examen final: "))*0.3
notaTrabajo=float(input("Nota trabajo final: "))*0.15
notaFinal= mediaParciales+notaEFinal+notaTrabajo

print("La nota final es:",notaFinal)