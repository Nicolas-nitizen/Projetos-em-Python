from random import randint
def abertura():
    logo_tipo = "JOGO DA FORCA!"
    print("=" * 30)
    print(f"{logo_tipo:^30}")
    print("=" * 30)

def jogar():
    abertura()

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    #enquato nao enforcou e nao aceitou - no caso as duas variaveis enforcou e acertou é True
    while not enforcou and not acertou:
        if chute in palavra_secreta:
            chute = input("Qua é o seu chute? ").strip().lower()
            pos = 0
            for l in palavra_secreta:
                if chute == l:
                    letras_acertadas[pos] = l

                pos += 1
        else:
            erros += 1
        enforcou = erros == 6
        print(letras_acertadas)


if __name__ == "__main__":
    jogar()