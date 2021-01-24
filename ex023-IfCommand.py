numero = (input("Digite um número de 0 a 9999, por favor! "))
while numero.__len__() < 4:
    input("Por favor digite um numero de 4 digitos: ")
    if numero.__len__() == 4:
        continue
        unidade = numero[3]
        print("Unidade: {}".format(unidade))
        dezena = numero[2]
        print("Dezena: {}".format(dezena))
        centena = numero[1]
        print("Centena: {}".format(centena))
        milhar = numero[0]
        print("Milhar: {}".format(milhar))
    else: quit()
else: quit()
