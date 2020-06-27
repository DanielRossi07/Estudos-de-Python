from random import shuffle
nom = str(input("Digite o primeiro nome: "))
nom1 = str(input("Digite o segundo nome: "))
non2 = str(input("Digite o terceiro nome: "))
nom3 = str(input("Digite o quarto nome: "))
lista = [nom, nom1, non2, nom3]
shuffle(lista)
print("Os sorteados foram: {}".format(lista))