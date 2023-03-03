from time import sleep
import adivinhacao
import forca

logo = "Escolhe o seu jogo!"
print("*" * 30)
print(f'{logo:^30}')
print('*' * 30)

print("(1) - Forca\n"
      "(2) - Adivinhação")

jogo = int(input("Qual jogo você escolhe: "))

if jogo == 1:
    print("Jogando forca!")
    sleep(3)
    forca.jogar()
elif jogo == 2:
    print("Jogando Advinhação!")
    sleep(3)
    adivinhacao.jogar()
