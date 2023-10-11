from conta import Conta

class PessoaJuridica(Conta):

    __Segundo_Titular = ''

    def __init__(self, titular, cnpj, saldo):
        super().__init__(6789, 'Pessoa Juridica')

        self.__Titular = titular
        self.__Cnpj = cnpj
        self.__Saldo = saldo


    @property
    def segundo_titular(self):
        return self.__Segundo_Titular
    
    @segundo_titular.setter
    def segundo_Titular(self, segundo_titular):
        self.__Segundo_Titular = segundo_titular
 
    @property
    def cnpj(self):
        return self.__Cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__Cnpj = cnpj
 
    @property
    def saldo(self):
        return self.__Saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__Saldo = saldo
 
    @property
    def titular(self):
        return self.__Titular
    
    @titular.setter
    def titular(self, titular):
        self.__Titular = titular


    def __str__(self):
        return f'\n{super().__str__()}   \nTitular: {self.titular} \nCnpj: {self.cnpj} \nSaldo: {self.saldo} \nSegundo Titular: {self.segundo_titular}'
 


