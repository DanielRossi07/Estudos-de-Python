menorpeso = ""
maiorpeso = ""
for c in range(1, 6):
    peso = input("Informe o seu peso: ")
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso <= menorpeso:
            menorpeso = peso
        if peso >= maiorpeso:
            maiorpeso = peso

print("O menor peso foi {} e o maior peso foi {}!".format(menorpeso, maiorpeso))