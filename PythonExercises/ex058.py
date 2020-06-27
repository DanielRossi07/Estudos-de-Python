import random
print("--- Jogo da adivinhação ---")
nome = str(input("Digite o seu nome para jogar: "))
print("O computador escolheu um número de 1 á 10...")


repostapc = random.randint(0, 10)
tentativas = 0
respostajogador = "-1"

while respostajogador != repostapc:
    respostajogador = int(input("Qual número você acha que ele escolheu? "))
    tentativas += 1

print("Você acertou, a resposta do PC foi {} e você tentou acertar {} vezes.".format(repostapc, tentativas))
