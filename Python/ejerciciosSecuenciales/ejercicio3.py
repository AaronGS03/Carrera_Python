#dados los catetos de un triángulo rectángulo, calcular hipotenusa

import math
cateto1 = float(input("Cat1: "))
cateto2 = float(input("Cat2: "))
print("Hipotenusa= %.2f"%(math.sqrt(cateto1**2+math.pow(cateto2,2))))
