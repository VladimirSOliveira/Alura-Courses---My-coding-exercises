import random

def jogar():
    print ("*" * 30)
    print ("meu programa de advinhacao")
    print ("*" * 30)

    numero_secreto = round (random.randrange (1,101))
    total_de_tentativas = 3
    pontos = 1000


    print ("qual o nível de dificuldade você quer?")
    print ("(1) FÁCIL (2) MODERADO (3) DIFÍCIL")
    nivel = int (input ("defina o seu nível: "))

    if (nivel == 1):
            total_de_tentativas = 20
    elif (nivel == 2):
            total_de_tentativas = 10
    else:
            total_de_tentativas = 5

    print(numero_secreto)

    for rodada in range (1, total_de_tentativas +1):
        print ("tentativa número: {} de {}" .format(rodada, total_de_tentativas))
        chute_str = input ("Qual o número correto? ")
        print ("você digitou ", chute_str)
        chute = int(chute_str)

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        if (acertou):
            print ("você acertou e fez {} pontos!" .format (pontos))
            break

        else:
            if(maior):
                print("você chutou um valor maior que o número secreto")
            elif(menor):
                print("você chutou um valor menor que o número secreto")

            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos

    print ("game over!!!")

if (__name__ == "__main__"):
    jogar()