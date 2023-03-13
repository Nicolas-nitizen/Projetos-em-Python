class Conta:
    def __int__(self, numero, titular, saldo, limite):
        print(f"Construindo Objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.despositar(valor)


usuario = Conta(123, "Nicolas", 66.0, 1000.0)
usuario.extrato()