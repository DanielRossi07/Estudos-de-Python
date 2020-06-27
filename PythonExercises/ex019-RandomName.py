import random
nom = str(input("Digite o primeiro nome: "))
nom1 = str(input("Digite o segundo nome: "))
nom2 = str(input("Digite o terceiro nome: "))
nom3 = str(input("Digite o quarto nome: "))
lista = [nom, nom1, nom2, nom3]
escolhido = random.choice(lista)
print("O sorteado foi: {}".format(escolhido))
