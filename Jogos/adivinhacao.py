from random import randint

def jogar():
    logo = "Jogo de Adivinhação"
    print("=" * 30)
    print(f"{logo:^30}")
    print("=" * 30)
    cont = 0
    numerosecreto = randint(0, 10)

    print("[1] - facil\n[2] - Medio\n[3] - Dificil ")
    opcoes = int(input("Qual é a sua opção: "))
    if opcoes == 1:
        tentativas = 20
    elif opcoes == 2:
        tentativas = 1
    else:
        tentativas = 5

    for c in range(0, tentativas):
        cont += 1
        print(f"Tentativa = {cont}")
        valor = int(input("Digite um valor: "))
        if valor == numerosecreto:
            print("Parabéns, voce acertou o numero secreto! {}".format(numerosecreto))
            print(f"O numeros de tentativas, foram {cont}")

        elif valor >= numerosecreto:
            print("O valor digitado, é maior que o numero secreto!")
        else:
            print("O valor digitado, é menor que o numero secreto!")
    print("FIM JOGO !!!")
if __name__ == "__main__":
    jogar()