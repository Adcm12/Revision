from conta import Conta

class PessoaFisica(Conta):

    __Segundo_Titular = ''

    def __init__(self, titular, cpf, saldo):
        super().__init__(1245, 'Pessoa Fisica')

        self.__Titular = titular
        self.__Cpf = cpf
        self.__Saldo = saldo


    @property
    def segundo_titular(self):
        return self.__Segundo_Titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__Segundo_Titular = segundo_titular
 
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
    def titular(self):
        return self.__Titular
    
    @titular.setter
    def titular(self, titular):
        self.__Titular = titular


    def __str__(self):
        return f'\n{super().__str__()}  \nTitular: {self.titular} \nCpf: {self.cpf} \nSaldo: {self.saldo} \nSegundo Titular: {self.segundo_titular}'
 


