import forca
import adivinhacao

def escolhe_jogo():
print ("*********************")
print ("Olá! Escolha seu jogo")
print ("*********************")

print("(1)forca   (2)adivinhacao")

jogo =  int(input("Qual Você escolhe?"))

if (jogo == 1):
    print ("quero jogar a forca")
    forca.jogar()
elif (jogo == 2):
    print ("quero jogar adivinhacao")
    adivinhacao.jogar()

if (__name__ == "__main__"):
    jogar()
