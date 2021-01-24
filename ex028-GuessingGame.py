import random
numero = random.randint (0,5)
print("-=-" * 20)
print("O computador vai pensar em um número, consegue advinhar?")
print("-=-" * 20)
resposta = int(input("Qual número de 0 a 5 você acha que o computador escolheu? "))
if resposta == numero:
    print("Voce acertou! O número era {}".format(numero))
else:
    print("Sinto muito, mas você errou! O número era {}!".format(numero))
print("Fim do jogo!!!")