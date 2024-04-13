""" El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido
desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. 
Para ello podemos hacer las siguientes subrutinas:

LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano. """

def leerFecha():
    dia= int(input("Dia: "))
    mes= int(input("Mes: "))
    año= int(input("Año: "))

    return [dia,mes,año]

d,m,a= leerFecha()

def EsBisiesto(año):
    return (año%4 == 0 and not (año%100 == 0))or año%400==0

def diaseDelMes(mes, año):
    if mes == 2:
        if EsBisiesto(año):
            return 29
        else:
            return 28
    elif mes in [4,6,9,11]:
        return 30
    else:
        return 31
    
def Calcular_Dia_Juliano(dia, mes,año):
    num=0
    for mes in range(1,mes):
        num=num+diaseDelMes(mes,año)
    num=num+dia
    return num

print(Calcular_Dia_Juliano(d,m,a))