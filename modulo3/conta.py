class Conta:
    
    def __init__(self, numero, titular, cpf, saldo, limite):

        print(f'Imprimindo variavel de referencia {self}')

        self.Numero : int = numero
        self.Titular : str = titular
        self.Cpf : str = cpf
        self.Saldo : float = saldo
        self.Limite : float = limite

