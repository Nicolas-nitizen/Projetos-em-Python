
class Conta:
    def __int__(self, numero, titular, saldo, limite):
        print(f"Construindo Objeto ... {self}")
        self.numero = 123
        self.titular = "Nicolas"
        self.saldo = 200.00
        self.limite = 1000.0

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

if __name__ in "__main__":
    Conta()