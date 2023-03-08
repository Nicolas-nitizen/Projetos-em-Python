from random import randint
def abertura():
    logo_tipo = "JOGO DA FORCA!"
    print("=" * 30)
    print(f"{logo_tipo:^30}")
    print("=" * 30)

def jogar():
    abertura()

    arquivo = open("palavras.txt", "a")
    palavras = []
    for linha in arquivo:
        linha = linha.lower().strip()
        palavras.append(linha)
    arquivo.close()

    pos_palavras = randint(0, len(palavras))
    palavra_secreta = palavras[pos_palavras]
    letras_acertadas = ["_" for l in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    #enquato nao enforcou e nao aceitou - no caso as duas variaveis enforcou e acertou é True
    while not enforcou and not acertou:

        chute = input("Qua é o seu chute? ").strip().lower()
        pos = 0
        if chute in palavra_secreta:
            for l in palavra_secreta:
                if chute == l:
                    letras_acertadas[pos] = l
                pos += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Parabéns! Você ganhou")
    elif enforcou:
        print("Infelizmente não foi dessa vez! Tente novamente.")
    print("FIM DO JOGO!!!")


if __name__ == "__main__":
    jogar()