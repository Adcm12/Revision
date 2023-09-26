class Casa:

    __Piso = 2

    def __init__(self, janelas, portas, quartos, banheiros, telhados, materiais_piso, materiais_portas):
        self.__Janelas : int = janelas
        self.__Portas : int = portas
        self.__Quartos : int = quartos
        self.__Banheiros : int = banheiros
        self.__Telhados : str = telhados
        self.__Materiais_piso : str = materiais_piso
        self.__Materiais_portas : str = materiais_portas

    #getters

    @property
    def janelas(self):
        return self.__Janelas
    
    @property
    def portas(self):
        return self.__Portas
    
    @property
    def quartos(self):
        return self.__Quartos
    
    @property
    def banheiros(self):
        return self.__Banheiros
    
    @property
    def telhados(self):
        return self.__Telhados
    
    @property
    def materiais_piso(self):
        return self.__Materiais_piso
    
    @property
    def materiais_portas(self):
        return self.__Materiais_portas
    
    @property
    def pisos(self):
        return self.__Piso
    
    #setters

    @janelas.setter
    def janelas(self, janela):
        self.__Janelas = janela
        
    @portas.setter
    def portas(self, porta):
        self.__Portas = porta

    @quartos.setter
    def quartos(self, quarto):
        self.__Quartos = quarto

    @banheiros.setter
    def banheiros(self, banheiro):
        self.__Banheiros = banheiro

    @telhados.setter
    def telhados(self, telhado):
        self.__Telhados = telhado

    @materiais_piso.setter
    def materiais_piso(self, materiais_piso):
        self.__Materiais_piso = materiais_piso

    @materiais_portas.setter
    def materiais_portas(self, materiais_porta):
        self.__Materiais_portas = materiais_porta


    def __str__(self):
        return f''' 
            \nNro piso : {self.pisos} 
            \nNro janelas : {self.janelas} 
            \nNro portas : {self.portas} 
            \nNro quartos : {self.quartos}
            \nNro banheiro :  {self.banheiros} 
            \nMateriais telhado : {self.telhados} 
            \nMateriais piso : {self.materiais_piso} 
            \nMateriais portas : {self.materiais_portas}
'''
