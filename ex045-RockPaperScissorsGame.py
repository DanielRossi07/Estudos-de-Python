import random
escolhas = ["pedra", "papel", "tesoura"]
escolhacomputador = random.choice(escolhas)
nome = input("Qual seu nome? ")
escolhajogador = input("Escolha entre pedra, papel ou tesoura: ").lower().strip()

if escolhajogador == escolhacomputador:
    print("O jogo empatou, os dois escolheram {}!".format(escolhacomputador))

elif escolhajogador == "papel" and escolhacomputador == "pedra":
    print("O {} escolheu {} e o computador {}, o {} ganhou!".format(nome, escolhajogador, escolhacomputador, nome))
elif escolhajogador == "tesoura" and escolhacomputador == "papel":
    print("O {} escolheu {} e o computador {}, o {} ganhou!".format(nome, escolhajogador, escolhacomputador, nome))
elif escolhajogador == "pedra" and escolhacomputador == "tesoura":
    print("O {} escolheu {} e o computador {}, o {} ganhou!".format(nome, escolhajogador, escolhacomputador, nome))

elif escolhacomputador == "papel" and escolhajogador == "pedra":
    print("O computador escolheu {} e o {} escolheu {}, o computador ganhou!".format(escolhacomputador, nome, escolhajogador))
elif escolhacomputador == "tesoura" and escolhajogador == "papel":
    print("O computador escolheu {} e o {} escolheu {}, o computador ganhou!".format(escolhacomputador, nome, escolhajogador))
elif escolhacomputador == "pedra" and escolhajogador == "tesoura":
    print("O computador escolheu {} e o {} escolheu {}, o computador ganhou!".format(escolhacomputador, nome, escolhajogador))

