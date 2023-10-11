class Conta:

    def __init__(self, numero, tipo):

        self.Numero = numero
        self.Tipo = tipo

    def __str__(self):
        return f'Número da conta: {self.Numero} \nTipo de conta: {self.Tipo}'
    

