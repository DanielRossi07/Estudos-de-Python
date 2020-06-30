numero = int(input("Digite um número: "))
resp = input("Deseja digitar mais um número? Insira S ou N: ")
numeros = numero
maiornum = numero
menornum = numero
contador = 1
media = numeros / contador

while resp == "S" or resp == "N":
    if resp == "S":
       numero = int(input("Digite um número: "))
       resp = input("Deseja digitar mais um número? Digite S ou N : ").strip().upper()
       numeros += numero
       contador += 1
       if maiornum < numero:
           maiornum = numero
       elif menornum > numero:
           menornum = numero
    elif resp == "N":
        print("Você digitou {}, o total foi {} e o número médio foi {}.".format(contador, numeros, media))
        print("E dentre os {} números o menor foi {} e o maior foi {}.".format(contador, menornum, maiornum))
        exit()