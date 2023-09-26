class Conta:

    __Numero = 123
    def __init__(self, numero, titular, cpf, saldo, limite):

        self.__Numero : int = numero
        self.__Titular : str = titular
        self.__Cpf : str = cpf
        self.__Saldo : float = saldo
        self.__Limite : float = limite

        @property
        def numero(self):
            return self.__Numero
        
        # @numero.setter        
        # def numero(self, numero):            
        #     self.__Numero = numero
        
        @property
        def titular(self):
            return self.__Titular
        
        @titular.setter        
        def titular(self, titular):
            self.__Titular = titular

        @property
        def cpf(self):
            return self.__Cpf
        
        @cpf.setter
        def cpf(self, cpf):
            self.__Cpf = cpf

        @property
        def saldo(self):
            return self.__Saldo
        
        @saldo.setter        
        def saldo(self, saldo):
            self.__Saldo = saldo

        
        @property
        def limite(self):
            return self.__Limite
        
        @limite.setter
        def limite(self, limite):
            self.__Limite = limite   


    def __str__(self):
        return f'{self.__numero} {self.__titular} {self.__cpf} {self.__saldo} {self.__limite}'
