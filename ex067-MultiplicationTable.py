while True:
    numero = int(input("Quer ver a tabuada de que número? "))
    if numero < 0:
        break
    cont = 0

    while cont != 11:
        soma = 0
        soma = numero * cont
        print("{} x {} = {}".format(numero, cont, soma))
        cont += 1
