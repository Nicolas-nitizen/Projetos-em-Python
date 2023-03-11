
def criar_conta(numero, titular, saldo, limite):
conta = {"Conta": numero, "Títular": titular, "Saldo": f"R${saldo:.2f}", "limite": f"R${limite:.2f}"}

def depositar(conta, valor):
    conta["Saldo"] += valor

def sacar(conta, valor):
    conta["Saldo"] -= valor

def extrato(conta):
    print(f'Saldo é {conta["Saldo"]}')