import random

corda = "=-=-=-=-=-=-=-=-=-=-=-=-="
linha = "-------------------------"
cont = 0
print(corda)
print("Vamos jogar PAR ou IMPAR")
print(corda)

while True:
    numerojogador = int(input("Digite o seu número: "))
    numeropc = random.randint(0, 10)
    soma = numerojogador + numeropc

    escolha = input("Par ou Impar? [P/I] ")
    if escolha == "I" or escolha == "i":
        escolha = "IMPAR"
    elif escolha == "P" or escolha == "p":
        escolha = "PAR"
    else:
        print("Opção invalida!")
        exit()

    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"

    print(linha)
    print("Você jogou {} e o Computador jogou {}. Total de {} deu {}".format(numerojogador, numeropc, soma, resultado))
    print(linha)

    if escolha == resultado:
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        print(corda)
        cont += 1
    else:
        print("Você PERDEU!")
        if cont == 1:
            print("GAME OVER! Você venceu {} vez.".format(cont))
            break
        else:
            print("GAME OVER! Você venceu {} vezes.".format(cont))
            break