class Vehiculo:

    __Modelo = 'Hibrido' #Un constructor es un metodo de responsabilidad unica, que permite inserir valores en los obejtos de la clase

    def __init__(self, cor, pineo, freio, combustivel):

        self.__Cor = cor
        self.__Pineo = pineo
        self.__Freio = freio
        self.__Combustivel = combustivel
        
    
    @property
    def modelo(self):
        return self.__Modelo
    
    @property
    def cor(self):
        return self.__Cor
    
    @property
    def pineo(self):
        return self.__Pineo
    
    @property
    def freio(self):
        return self.__Freio
    
    @property
    def combustivel(self):
        return self.__Combustivel
    

    @cor.setter
    def cor(self, cor):
        self.__Cor = cor
    
    @pineo.setter
    def pineo(self, pineo):
        self.__Pineo = pineo
    
    @freio.setter
    def freio(self, freio):
        self.__Freio = freio
    
    @combustivel.setter
    def combustivel(self, combustivel):
        self.__Combustivel = combustivel

    def __str__(self):
        return f'''\nModelo: {self.modelo} 
                \nCor : {self.cor}
                \nPineo : {self.pineo}
                \nFreio : {self.freio}
                \nCombustivel : {self.combustivel}
'''
    
vehiculo1 = Vehiculo('Preto', 'radial', 'Abs', 'Gasolina' )

print(vehiculo1)