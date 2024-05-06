""" Realizar clase "DNI" guardar número DNI (guardar en str de len=8)
y letra correspondiente. Crear método mostrar, y la letra se calcula 
automáticamente"""

class DNI():
    
    @property
    def num(self):
        return self.num
    
    @property
    def letra(self):
        return self.letra

    @num.setter
    def num(self,num):
        if len(num)==8 and num.isdigit():
            self._num=num
            self.letra=self.__calcularLetra()
        else:
            self._num=0
            self._letra=""
            print("DNI Incorrecto")

    @property
    def letra(self):
        return self.letra
    
    def __init__(self, num):
        self.num=num

    #que tenga __ delante hace que sea un método oculto, privado, 
    #por lo que no podrá usarse fuera de la clase
    def __calcularLetra(self):
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(self.num)%23]
    
    def mostrar(self):
        print(self.num,self.letra)


    